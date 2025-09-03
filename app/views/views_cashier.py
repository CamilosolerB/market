from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import transaction, IntegrityError
from fpdf import FPDF
from .. import models
import json
import datetime
import uuid
from . import email

def cashier_page(request):
    if request.session.get('cajero'):
        stats = models.stats.objects.all()[0]
        cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
        return render(request,'cashier/home_cash.html', {'stats':stats,'data': cashier, 'color': 'danger'})
    else: 
        return redirect('/singout/')
    
def inventory_page(request):
    if request.session.get('cajero'):
        cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
        products = models.Producto.objects.all()
        return render(request,'cashier/inventario.html', {'data': cashier, 'color': 'danger', 'products' : products})
    else: 
        return redirect('/singout/')
    
@csrf_exempt
@require_http_methods(["POST"])
def get_product(request):
    if request.session.get('cajero'):
        try:
            data = json.loads(request.body)
            id = data.get('id')
            nombre = data.get('nombre')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        if id:
            product_data = models.Producto.objects.filter(idProducto=id).values()
        elif nombre:
            product_data = models.Producto.objects.filter(nombreProducto=nombre).values()
        else:
            return JsonResponse({'error': 'No se proporcionó ID o nombre'}, status=400)
        if not product_data:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)
        return JsonResponse(list(product_data), safe=False)
    else:
        return redirect('/signout/')
    
@require_http_methods(['POST'])
@csrf_exempt
def finish_shop(request):
    if request.session.get('cajero'):
        data = json.loads(request.body)
        client = create_or_update_clients(data.get('cliente'))
        cashier = models.Cajero.objects.get(idCajero=request.session.get('id'))
        factura_id = int(uuid.uuid4().int & (1 << 32)-1)
        fisica = data.get('fisico')
        digital = data.get('digital')
        print(data)
        try:
            with transaction.atomic():
                factura = models.Factura(
                    idFactura=factura_id,
                    cedulaCliente=client,
                    idCajero=cashier,
                    totalBruto=data.get('subtotal'),
                    subTotal=data.get('total'),
                    totalIva=data.get('iva')
                )
                factura.save()
                list_products = data.get('productos')
                if fisica & digital:
                    pdflink = generate_pdf(client, cashier, factura, list_products)
                    factura.link = pdflink
                    factura.save()
                    email.send_email(client.correo, factura)
                elif fisica:
                    pdflink = generate_pdf(client, cashier, factura, list_products)
                    factura.link = pdflink
                    factura.save()
                elif digital:
                    pdflink = generate_pdf(client, cashier, factura, list_products)
                    factura.link = pdflink
                    factura.save()
                    create_compra(list_products, factura)
                    return JsonResponse(success=True)
                create_compra(list_products, factura)
        except IntegrityError as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'link': pdflink})
    else:
        return redirect('/singout/')

    
def create_compra(lista, factura): 
    for i in range(len(lista)): 
        product = models.Producto.objects.get(idProducto=lista[i][0]) 
        quantity = lista[i][4] 
        total = lista[i][5] 
        utilidad = float(lista[i][5]) - float(lista[i][2]) 
        models.Compra.objects.create(idProducto=product, cantidad=quantity, total=total, utilidad=utilidad, idFactura=factura)
        

def create_or_update_clients(cliente):
    try:
        client = models.Cliente.objects.get(cedula=cliente[0])
        client.nombreCliente = cliente[1]
        client.numeroCompras += 1
        client.correo = cliente[2]
        client.telefono = cliente[3]
        client.save()
    except models.Cliente.DoesNotExist:
        client = models.Cliente(cedula=cliente[0], nombreCliente=cliente[1], numeroCompras=1, correo=cliente[2], telefono=cliente[3])
        client.save()
    return client
    
@require_http_methods(['POST'])
@csrf_exempt
def search_client(request):
    if request.session.get('cajero'):
        data = json.loads(request.body)
        dni = data.get('dni');
        client = models.Cliente.objects.filter(cedula=dni).values()
        if not client:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
        else:
            return JsonResponse(list(client), safe=False)
    else:
        return redirect('/singout/')

def generate_pdf(client, cashier, factura, compras):
    factura.save()
    # Crear instancia de FPDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    # Contenido del encabezado
    pdf.set_font('Arial', '', 12)
    pdf.cell(w=0, h=10, txt='Factura No: {}'.format(factura.idFactura), ln=True)
    pdf.cell(w=0, h=10, txt='Cliente: {}'.format(client.nombreCliente), ln=True)
    pdf.cell(w=0, h=10, txt='CC: {}'.format(client.cedula), ln=True)
    pdf.cell(w=0, h=10, txt='Teléfono: {}'.format(client.telefono), ln=True)
    pdf.cell(w=0, h=10, txt='Correo: {}'.format(client.correo), ln=True)
    pdf.cell(w=0, h=10, txt='Cajero: {}'.format(cashier.nombreCajero), ln=True)
    pdf.cell(w=0, h=10, txt='Fecha: {}'.format(factura.day), ln=True)

    # Insertar logo
    url = 'https://www.youtube.com/watch?v=Rf2ESIWKtJw&pp=ygUVY29tbyBkaWNlbiBsb3MgcGVycm9z'
    pdf.image('app/static/img/logo.jpeg', x=120, y=20, w=70, h=20, link=url)

    # Agregar tabla de compras
    pdf.set_font('Arial', '', 12)
    pdf.cell(w=33, h=15, txt='id', border='BT', align='C', fill=0)
    pdf.cell(w=33, h=15, txt='Producto', border='BT', align='C', fill=0)
    pdf.cell(w=33, h=15, txt='Precio unitario', border='BT', align='C', fill=0)
    pdf.cell(w=33, h=15, txt='Iva', border='BT', align='C', fill=0)
    pdf.cell(w=33, h=15, txt='Cantidad', border='BT', align='C', fill=0)
    pdf.cell(w=33, h=15, txt='Precio total', border='BT', align='C', fill=0)
    pdf.ln(10)  # Salto de línea
    for compra in compras:
        pdf.cell(w=33, h=20, txt=str(compra[0]), border=0, align='C')  # Accede al primer elemento de la compra
        pdf.cell(w=33, h=20, txt=compra[1], border=0, align='C')        # Accede al segundo elemento de la compra
        pdf.cell(w=33, h=20, txt=str(compra[2]), border=0, align='C')    # Accede al tercer elemento de la compra
        pdf.cell(w=33, h=20, txt=str(compra[3] + '%'), border=0, align='C')  # Accede al cuarto elemento de la compra
        pdf.cell(w=33, h=20, txt=str(compra[4]), border=0, align='C')    # Accede al quinto elemento de la compra
        pdf.cell(w=33, h=20, txt=str(compra[5]), border=0, align='C')    # Accede al sexto elemento de la compra
        pdf.ln(10)  # Salto de línea
    pdf.ln(10)
    pdf.cell(w=0, h=10, txt='Subtotal: {}'.format(factura.totalBruto), ln=True, align='R')
    pdf.cell(w=0, h=10, txt='Total Iva: {}'.format(factura.totalIva), ln=True, align='R')
    pdf.cell(w=0, h=10, txt='Total: {}'.format(factura.subTotal), ln=True, align='R')

    # Guardar el PDF
    fecha = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    pdf.output('app/static/facturas/recibo'+fecha+'.pdf')
    return '/static/facturas/recibo'+fecha+'.pdf/'

