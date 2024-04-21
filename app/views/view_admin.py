from django.shortcuts import render, redirect
from .. import models
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
import openpyxl
from django.core.files.storage import FileSystemStorage

def home_page_admin(request):
    if request.session.get('admin'):
        providers = models.Proveedor.objects.all()
        product = models.Producto.objects.all()
        return render(request,'./admin/home_admin.html', {'data': product, 'providers': providers, 'color': 'primary'})
    else:
        return redirect('/singout/')

def provider_page(request):
    if request.session.get('admin'):
        provider = models.Proveedor.objects.all()
        return render(request, './admin/provide_mod.html', {'data': provider, 'color': 'primary'})
    else:
        return redirect('/singout/')
    
def admin_interface(request):
    if request.session.get('admin'):
        admin = models.admin.objects.all()
        return render(request, './admin/admin_mod.html', {'admin': admin, 'color': 'primary'})

    else:
        return redirect('/singout/')
    
def cashier_admin(request):
    if request.session.get('admin'):
        cashier = models.Cajero.objects.all()
        return render(request, './admin/cashier_mod.html', {'data': cashier, 'color': 'primary'})
    else:
        return redirect('/singout/')
    
def qr_admin(request):
    if request.session.get('admin'):
        stats = models.stats.objects.all()[0]
        return render(request, './admin/qr_page.html', {'stats':stats,'color': 'primary'})
    else:
        return redirect('/singout/')
    
def create_product(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            nombre = post.get('nombre')
            precio = post.get('precio')
            cantidad = post.get('cantidad')
            unidad = post.get('unidad')
            iva = float(post.get('iva')) / 100
            unidad = post.get('unidad')
            iva = float(post.get('iva')) / 100
            idprovider = post.get('provider')
            provider = models.Proveedor.objects.get(nitProvider=idprovider)
            models.Producto.objects.create(nombreProducto=nombre, precioCompra=precio, 
                                           ivaProducto=iva, stockProducto=cantidad, unidadMedida = unidad,
                                           nitProveedor = provider)
            return redirect('/admin/')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')
    
def create_admin(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            email = post.get('email')
            password = post.get('password')
            clave = make_password(password)
            admin = models.admin.objects.create(email=email, password=clave)
            return redirect('/admin/admins')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')
    
def create_cashier(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            nombre = post.get('nombre')
            salario = post.get('salario')
            correo = post.get('correo')
            password = post.get('password')
            password = make_password(password)
            models.Cajero.objects.create(nombreCajero = nombre, salario = salario,
                                          correo = correo, password = password)
            return redirect('/admin/cashiers')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')
            
def create_provider(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            nit = post.get('nit')
            nombre = post.get('nombre')
            models.Proveedor.objects.create(nitProvider=nit, nomProvider = nombre)
            return redirect('/admin/providers')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')
    
def update_product(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            modelo = models.Producto()
            modelo.idProducto = post.get('id')
            modelo.nombreProducto = post.get('nombre')
            modelo.precioCompra = post.get('precio')
            modelo.stockProducto = post.get('cantidad')
            modelo.unidadMedidad = post.get('unidad')
            modelo.unidadMedidad = post.get('unidad')
            modelo.ivaProducto = float(post.get('iva'))
            idprovider = post.get('provider')
            modelo.nitProveedor = models.Proveedor.objects.get(nitProvider=idprovider)
            modelo.save()
            return redirect('/admin/')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')

def update_admin(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            modelo = models.admin()
            modelo.id = post.get('id')
            modelo.email = post.get('email')
            password = post.get('password')
            modelo.password = make_password(password)
            modelo.save()
            return redirect('/admin/admins')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')

def update_cashier(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            modelo = models.Cajero()
            modelo.idCajero = post.get('id')
            modelo.nombreCajero = post.get('nombre')
            modelo.salario = post.get('salario')
            modelo.correo = post.get('correo')
            password = post.get('password')
            modelo.password = make_password(password)
            modelo.save()
            return redirect('/admin/cashiers')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')

def update_provider(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            modelo = models.Proveedor()
            modelo.nitProvider = post.get('nit')
            modelo.nomProvider = post.get('nombre')
            modelo.save()
            return redirect('/admin/providers')
        else:
            return redirect('/admin/')
    else:
        return redirect('/singout/')

    
    
def delete_admin(request, id):
    if request.session.get('admin'):
        try:
            admin = models.admin.objects.get(id=id)
            admin.delete()
            return JsonResponse({'mensaje': 'Administrador eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar.'}, status=404)
    else:
        return redirect('/singout/')
        
def delete_product(request, id):
    if request.session.get('admin'):
        try:
            admin = models.Producto.objects.get(idProducto=id)
            admin.delete()
            return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar este producto.'}, status=404)
    else:
        return redirect('/singout/')

        
def delete_cashier(request, id):
    if request.session.get('admin'):
        try:
            cajero = models.Cajero.objects.get(idCajero=id)
            cajero.delete()
            return JsonResponse({'mensaje': 'Cajero eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar el cajero.'}, status=404)
    else:
        return redirect('/singout/')
        
def delete_provider(request, id):
    if request.session.get('admin'):
        try:
            provider = models.Proveedor.objects.get(nitProvider=id)
            provider.delete()
            return JsonResponse({'mensaje': 'Cajero eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar el cajero.'}, status=404)
    else:
        return redirect('/singout/')
def generate_excel_product(request):
    if request.session.get('admin'):
        products = models.Producto.objects.all()
        wb = openpyxl.Workbook()
        hoja1 = wb.create_sheet("Productos")
        hoja1.append(('ID', 'Nombre', 'Precio', 'IVA', 'Stock', 'NIT','Nombre Compañia'))
        for product in products:
            product_data = [
                product.idProducto,
                product.nombreProducto,
                product.precioCompra,
                product.ivaProducto,
                product.stockProducto,
                product.nitProveedor.nitProvider,
                product.nitProveedor.nomProvider
            ]
            hoja1.append(product_data)
    if request.session.get('admin'):
        products = models.Producto.objects.all()
        wb = openpyxl.Workbook()
        hoja1 = wb.create_sheet("Productos")
        hoja1.append(('ID', 'Nombre', 'Precio', 'IVA', 'Stock', 'NIT','Nombre Compañia'))
        for product in products:
            product_data = [
                product.idProducto,
                product.nombreProducto,
                product.precioCompra,
                product.ivaProducto,
                product.stockProducto,
                product.nitProveedor.nitProvider,
                product.nitProveedor.nomProvider
            ]
            hoja1.append(product_data)

        # Guardar el libro de Excel en la respuesta HTTP para descargar
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
        wb.save(response)
        # Guardar el libro de Excel en la respuesta HTTP para descargar
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=productos.xlsx'
        wb.save(response)

        return response
    else:
        return redirect('/singout/')
    
def create_nequi_qr(request):
    if request.session.get('admin'):
        qr = models.stats.objects.all()[0]
        myFile = request.FILES['qrcode']
        fs = FileSystemStorage()
        dirfile = 'app/static/img/'+myFile.name
        filename = fs.save(dirfile, myFile)
        qr.nequi = '/img/'+myFile.name
        qr.save()
        return redirect('/admin/qrpage/')
    else:
        return redirect('/singout/')
    
def create_nequi_qr(request):
    if request.session.get('admin'):
        qr = models.stats.objects.all()[0]
        myFile = request.FILES['qrcode']
        fs = FileSystemStorage()
        dirfile = 'app/static/img/'+myFile.name
        filename = fs.save(dirfile, myFile)
        qr.daviplata = '/img/'+myFile.name
        qr.save()
        return redirect('/admin/qrpage/')
    else:
        return redirect('/singout/')