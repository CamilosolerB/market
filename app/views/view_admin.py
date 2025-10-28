from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import io
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from app.forms import Cliente
from app.models import Cliente 


from .. import models



# --- PÁGINAS PRINCIPALES ---
def home_page_admin(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    providers = models.Proveedor.objects.all()
    products = models.Producto.objects.all()
    return render(request, './admin/home_admin.html', {'data': products, 'providers': providers, 'color': 'primary'})


def provider_page(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    providers = models.Proveedor.objects.all()
    return render(request, './admin/provide_mod.html', {'data': providers, 'color': 'primary'})


def admin_interface(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    admins = models.admin.objects.all()
    return render(request, './admin/admin_mod.html', {'admin': admins, 'color': 'primary'})

def qr_admin(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    stats = models.stats.objects.first()
    return render(request, './admin/qr_page.html', {'stats': stats, 'color': 'primary'})


# --- FUNCIONES AUXILIARES ---
def get_proveedor(val):
    if val:
        return models.Proveedor.objects.filter(nitProvider=val).first()
    return None


# --- CRUD PRODUCTOS ---
def create_product(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        producto = models.Producto(
            nombreProducto=post.get('nombreProducto'),
            nombreGenerico=post.get('nombreGenerico'),
            stockProducto=post.get('stockProducto'),
            unidadMedida=post.get('unidadMedida'),
            ubicacion=post.get('ubicacion'),
            cantAdquirida=post.get('cantAdquirida'),
            proveedorPrincipal=get_proveedor(post.get('proveedorPrincipal')),
            proveedorSuplente=get_proveedor(post.get('proveedorSuplente')),
            proveedor3=get_proveedor(post.get('proveedor3')),
            proveedor4=get_proveedor(post.get('proveedor4')),
        )
        producto.save()
        return redirect('/admin/')
    return redirect('/admin/')


def update_product(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    
    if request.method == 'POST':
        post = request.POST
        try:
            producto = models.Producto.objects.get(idProducto=post.get('idProducto'))
        except models.Producto.DoesNotExist:
            return redirect('/admin/')  # Si no existe, volver al listado

        # Actualizar los campos solo si vienen en POST
        producto.nombreProducto = post.get('nombreProducto', producto.nombreProducto)
        producto.nombreGenerico = post.get('nombreGenerico', producto.nombreGenerico)
        producto.stockProducto = post.get('stockProducto', producto.stockProducto)
        producto.unidadMedida = post.get('unidadMedida', producto.unidadMedida)
        producto.ubicacion = post.get('ubicacion', producto.ubicacion)
        producto.cantAdquirida = post.get('cantAdquirida', producto.cantAdquirida)

        # Proveedores
        producto.proveedorPrincipal = get_proveedor(post.get('proveedorPrincipal'))
        producto.proveedorSuplente = get_proveedor(post.get('proveedorSuplente'))
        producto.proveedor3 = get_proveedor(post.get('proveedor3'))
        producto.proveedor4 = get_proveedor(post.get('proveedor4'))

        producto.save()
        return redirect('/admin/')
    
    return redirect('/admin/')

def delete_product(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        product = models.Producto.objects.get(idProducto=id)
        product.delete()
        return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
    except models.Producto.DoesNotExist:
        return JsonResponse({'error': 'No se pudo eliminar el producto.'}, status=404)


# --- CRUD ADMIN ---
def create_admin(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        email = post.get('email')
        password = make_password(post.get('password'))
        models.admin.objects.create(email=email, password=password)
        return redirect('/admin/admins')
    return redirect('/admin/')


def update_admin(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        admin_obj = models.admin.objects.get(id=post.get('id'))
        admin_obj.email = post.get('email')
        admin_obj.password = make_password(post.get('password'))
        admin_obj.save()
        return redirect('/admin/admins')
    return redirect('/admin/')


def delete_admin(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        admin_obj = models.admin.objects.get(id=id)
        admin_obj.delete()
        return JsonResponse({'mensaje': 'Administrador eliminado correctamente'})
    except models.admin.DoesNotExist:
        return JsonResponse({'error': 'No se pudo eliminar.'}, status=404)



# ---------- CRUD ALMACEN------------

def storage_page(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    
    # Traer todos los items de almacén
    data = models.StorageItem.objects.all()
    
    # Renderizar usando tu template actual
    return render(request, 'admin/storage_mod.html', {'data': data, 'color': 'primary'})

def create_storage_item(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        models.StorageItem.objects.create(
            item_name=post.get('item'),
            quantity=post.get('cantidad')
        )
        return redirect('/admin/storage/')
    return redirect('/admin/')

def update_storage_item(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        item = models.StorageItem.objects.get(idItem=post.get('id'))
        item.item_name = post.get('item')
        item.quantity = post.get('cantidad')
        item.save()
        return redirect('/admin/storage/')
    return redirect('/admin/')

def delete_storage_item(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        item = models.StorageItem.objects.get(idItem=id)
        item.delete()
        return JsonResponse({'mensaje': 'Item eliminado correctamente'})
    except models.StorageItem.DoesNotExist:
        return JsonResponse({'error': 'No se pudo eliminar el item.'}, status=404)


# --- CRUD PROVEEDOR ---
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .. import models

def provider_page(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    providers = models.Proveedor.objects.all()
    return render(request, './admin/provide_mod.html', {'data': providers, 'color': 'primary'})


def create_provider(request):
    if not request.session.get('admin'):
        return redirect('/singout/')

    if request.method == 'POST':
        post = request.POST
        nit = post.get('codProveedor')
        nombre = post.get('nomProveedor')

        # Validación básica
        if not nit or not nombre:
            messages.error(request, "Debe ingresar el NIT y el nombre del proveedor.")
            return redirect('/admin/create_provider/')

        # Verificar si ya existe un proveedor con ese NIT
        if models.Proveedor.objects.filter(nit=nit).exists():
            messages.error(request, f"El NIT {nit} ya está registrado.")
            return redirect('/admin/create_provider/')

        models.Proveedor.objects.create(
            nit=nit,
            nombre=nombre,
            contacto=post.get('contacto'),
            direccion=post.get('direccion'),
            telefono=post.get('telefono'),
            celular=post.get('celular'),
            web=post.get('web'),
            correo=post.get('correo'),
            codigoMat=post.get('codigoMat'),
            nombreProducto=post.get('nombreProducto'),
            precio=post.get('precio'),
            unidadMedida=post.get('unidadMedida'),
            unidadCompra=post.get('unidadCompra'),
            unidadMinCompra=post.get('unidadMinCompra'),
            leadTimeDias=post.get('leadTimeDias'),
            medioTransporte=post.get('medioTransporte'),
            reabastecimiento=post.get('reabastecimiento'),
            terminoPago=post.get('terminoPago'),
            tiempoCreditoDias=post.get('tiempoCreditoDias')
        )
        messages.success(request, "Proveedor creado correctamente.")
        return redirect('/admin/providers/')

    return redirect('/admin/')



def update_provider(request):
    if not request.session.get('admin'):
        return redirect('/singout/')

    if request.method == 'POST':
        post = request.POST
        nit = post.get('codProveedor')
        nombre = post.get('nomProveedor')

        if not nit or not nombre:
            messages.error(request, "Debe ingresar el NIT y el nombre del proveedor.")
            return redirect('/admin/providers/')

        try:
            provider = models.Proveedor.objects.get(nit=nit)
        except models.Proveedor.DoesNotExist:
            messages.error(request, "Proveedor no encontrado.")
            return redirect('/admin/providers/')

        # Actualizar campos
        provider.nombre = nombre
        provider.contacto = post.get('contacto')
        provider.direccion = post.get('direccion')
        provider.telefono = post.get('telefono')
        provider.celular = post.get('celular')
        provider.web = post.get('web')
        provider.correo = post.get('correo')
        provider.codigoMat = post.get('codigoMat')
        provider.nombreProducto = post.get('nombreProducto')
        provider.precio = post.get('precio')
        provider.unidadMedida = post.get('unidadMedida')
        provider.unidadCompra = post.get('unidadCompra')
        provider.unidadMinCompra = post.get('unidadMinCompra')
        provider.leadTimeDias = post.get('leadTimeDias')
        provider.medioTransporte = post.get('medioTransporte')
        provider.reabastecimiento = post.get('reabastecimiento')
        provider.terminoPago = post.get('terminoPago')
        provider.tiempoCreditoDias = post.get('tiempoCreditoDias')

        provider.save()
        messages.success(request, "Proveedor actualizado correctamente.")
        return redirect('/admin/providers/')

    return redirect('/admin/')


def delete_provider(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        provider = models.Proveedor.objects.get(codProveedor=id)
        provider.delete()
        return JsonResponse({'mensaje': 'Proveedor eliminado correctamente'})
    except models.Proveedor.DoesNotExist:
        return JsonResponse({'error': 'No se pudo eliminar el proveedor.'}, status=404)

from django.shortcuts import render, redirect
from .. import models

# --------------- CRID BODEGA ------------

def bodega_page(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    items = models.Bodega.objects.all()
    return render(request, './admin/bodega.html', {'bodega_items': items, 'color': 'primary'})

def create_bodega(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    if request.method == 'POST':
        post = request.POST
        codigo = post.get('codigo')

        # Validar si el código ya existe
        if models.Bodega.objects.filter(codigo=codigo).exists():
            # Aquí puedes enviar un mensaje de error o alertar
            return redirect('/admin/bodega/')  

        try:
            models.Bodega.objects.create(
                ubicacion=post.get('ubicacion'),
                nivel=post.get('nivel'),
                posicion=post.get('posicion'),
                localizador=post.get('localizador'),
                codigo=codigo,
                descripcion=post.get('descripcion'),
                cantidad=post.get('cantidad'),
                unidad=post.get('unidad')
            )
        except IntegrityError:
            return redirect('/admin/bodega/')
        return redirect('/admin/bodega/')
    return redirect('/admin/bodega/')

def update_bodega(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        item = models.Bodega.objects.get(id=id)
    except models.Bodega.DoesNotExist:
        return redirect('/admin/bodega/')

    if request.method == 'POST':
        post = request.POST
        # Validar que no exista otro item con el mismo código
        codigo_nuevo = post.get('codigo', item.codigo)
        if models.Bodega.objects.filter(codigo=codigo_nuevo).exclude(id=item.id).exists():
            return redirect('/admin/bodega/')

        item.ubicacion = post.get('ubicacion', item.ubicacion)
        item.nivel = post.get('nivel', item.nivel)
        item.posicion = post.get('posicion', item.posicion)
        item.localizador = post.get('localizador', item.localizador)
        item.codigo = codigo_nuevo
        item.descripcion = post.get('descripcion', item.descripcion)
        item.cantidad = post.get('cantidad', item.cantidad)
        item.unidad = post.get('unidad', item.unidad)
        item.save()
        return redirect('/admin/bodega/')
    return redirect('/admin/bodega/')

def delete_bodega(request, id):
    if not request.session.get('admin'):
        return redirect('/singout/')
    try:
        item = models.Bodega.objects.get(id=id)
        item.delete()
    except models.Bodega.DoesNotExist:
        pass
    return redirect('/admin/bodega/')


# ---------- CRUD CLIENTE --------------
def clientes_page(request):
    clientes = Cliente.objects.all()
    return render(request, 'admin/clientes.html', {'clientes': clientes})

def create_cliente(request):
    if request.method == 'POST':
        # Los nombres de los campos deben coincidir con los del formulario HTML
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre_cliente')
        razon_social = request.POST.get('razon_social')
        telefono = request.POST.get('telefono')
        contacto = request.POST.get('contacto')
        correo = request.POST.get('correo')
        ciudad = request.POST.get('ciudad')
        tipo_agua = request.POST.get('tipo_agua')
        cantidad_promedio_kg = request.POST.get('cantidad_promedio_kg')

        # Crear cliente
        Cliente.objects.create(
            codigo=codigo,
            nombre=nombre,
            razon_social=razon_social,
            telefono=telefono,
            contacto=contacto,
            correo=correo,
            ciudad=ciudad,
            tipo_agua=tipo_agua,
            cantidad_promedio_kg=cantidad_promedio_kg
        )

        messages.success(request, 'Cliente creado exitosamente')
        return redirect('clientes_page')
    return redirect('clientes_page')


def update_cliente(request, codigo):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(codigo=codigo)
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente no encontrado')
            return redirect('clientes_page')

        # Actualizar campos según los nombres del formulario
        cliente.nombre = request.POST.get('nombre_cliente', cliente.nombre)
        cliente.razon_social = request.POST.get('razon_social', cliente.razon_social)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.contacto = request.POST.get('contacto', cliente.contacto)
        cliente.correo = request.POST.get('correo', cliente.correo)
        cliente.ciudad = request.POST.get('ciudad', cliente.ciudad)
        cliente.tipo_agua = request.POST.get('tipo_agua', cliente.tipo_agua)
        cliente.cantidad_promedio_kg = request.POST.get('cantidad_promedio_kg', cliente.cantidad_promedio_kg)

        cliente.save()
        messages.success(request, 'Cliente actualizado correctamente')
        return redirect('clientes_page')
    return redirect('clientes_page')


def delete_cliente(request, codigo):
    try:
        cliente = Cliente.objects.get(codigo=codigo)
        cliente.delete()
        messages.success(request, 'Cliente eliminado correctamente')
    except Cliente.DoesNotExist:
        messages.error(request, 'Cliente no encontrado')
    return redirect('clientes_page')

# ==============EXPORTAR A EXCEL =======================================

def generate_excel_product(request):
    productos = models.Producto.objects.all()

    # Crear libro y hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventario"

    # Encabezados
    headers = [
        "CÓDIGO", "NOMBRE DEL PRODUCTO", "NOMBRE GENÉRICO",
        "TOTAL INVENTARIO", "UNIDAD DE MEDIDA", "UBICACIÓN",
        "CANTIDAD ADQUIRIDA", "PROVEEDOR PRINCIPAL", "PROVEEDOR SUPLENTE",
        "PROVEEDOR 3", "PROVEEDOR 4"
    ]
    ws.append(headers)

    # Filas de datos
    for p in productos:
        ws.append([
            p.idProducto,
            p.nombreProducto,
            p.nombreGenerico or '',
            p.stockProducto,
            p.unidadMedida or '',
            p.ubicacion or '',
            p.cantAdquirida or '',
            p.proveedorPrincipal.nomProvider if p.proveedorPrincipal else '',
            p.proveedorSuplente.nomProvider if p.proveedorSuplente else '',
            p.proveedor3.nomProvider if p.proveedor3 else '',
            p.proveedor4.nomProvider if p.proveedor4 else '',
        ])

    # Guardar en memoria
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="inventario.xlsx"'
    wb.save(response)
    return response


# =====================================================
# EXPORTAR A PDF
# =====================================================
def generate_pdf_product(request):
    productos = models.Producto.objects.all()

    buffer = io.BytesIO()
    from reportlab.pdfgen import canvas

    # Crear PDF en modo horizontal
    c = canvas.Canvas(buffer, pagesize=landscape(letter))
    width, height = landscape(letter)

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 40, "Reporte de Inventario")

    # Preparar datos para la tabla
    data = [[
        "CÓDIGO", "NOMBRE DEL PRODUCTO", "NOMBRE GENÉRICO",
        "TOTAL INVENTARIO", "UNIDAD DE MEDIDA", "UBICACIÓN",
        "CANT. ADQUIRIDA", "PROV. PRINCIPAL", "PROV. SUPLENTE",
        "PROV. 3", "PROV. 4"
    ]]

    for p in productos:
        data.append([
            str(p.idProducto),
            p.nombreProducto or '',
            p.nombreGenerico or '',
            str(p.stockProducto),
            p.unidadMedida or '',
            p.ubicacion or '',
            str(p.cantAdquirida or ''),
            p.proveedorPrincipal.nomProvider if p.proveedorPrincipal else '',
            p.proveedorSuplente.nomProvider if p.proveedorSuplente else '',
            p.proveedor3.nomProvider if p.proveedor3 else '',
            p.proveedor4.nomProvider if p.proveedor4 else '',
        ])

    # Crear tabla
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E7DB7')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    # Ajustar posición de la tabla
    width_available = width - 80
    height_available = height - 100
    table.wrapOn(c, width_available, height_available)
    table.drawOn(c, 40, height_available - len(data) * 15)

    # Finalizar PDF
    c.showPage()
    c.save()
    buffer.seek(0)

    return HttpResponse(buffer, content_type='application/pdf')

# --- QR ---
def create_nequi_qr(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    qr = models.stats.objects.first()
    myFile = request.FILES['qrcode']
    fs = FileSystemStorage()
    filename = fs.save('app/static/img/' + myFile.name, myFile)
    qr.nequi = '/img/' + myFile.name
    qr.save()
    return redirect('/admin/qrpage/')


def create_daviplata_qr(request):
    if not request.session.get('admin'):
        return redirect('/singout/')
    qr = models.stats.objects.first()
    myFile = request.FILES['qrcode']
    fs = FileSystemStorage()
    filename = fs.save('app/static/img/' + myFile.name, myFile)
    qr.daviplata = '/img/' + myFile.name
    qr.save()
    return redirect('/admin/qrpage/')
