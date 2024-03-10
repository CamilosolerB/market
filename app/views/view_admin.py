from django.shortcuts import render, redirect
from .. import models
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
import openpyxl
#

def home_page_admin(request):
    if request.session.get('admin'):
        providers = models.Proveedor.objects.all()
        product = models.Producto.objects.all()
        return render(request,'./admin/home_admin.html', {'data': product, 'providers': providers})
    else:
        return redirect('/')

def provider_page(request):
    if request.session.get('admin'):
        provider = models.Proveedor.objects.all()
        return render(request, './admin/provide_mod.html', {'data': provider})
    else:
        return redirect('/')
    
def admin_interface(request):
    if request.session.get('admin'):
        admin = models.admin.objects.all()
        return render(request, './admin/admin_mod.html', {'admin': admin})
    else:
        return redirect('/')
    
def cashier_admin(request):
    if request.session.get('admin'):
        cashier = models.Cajero.objects.all()
        return render(request, './admin/cashier_mod.html', {'data': cashier})
    else:
        return redirect('/')
    
def create_product(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            nombre = post.get('nombre')
            precio = post.get('precio')
            cantidad = post.get('cantidad')
            iva = float(post.get('iva'))
            idprovider = post.get('provider')
            provider = models.Proveedor.objects.get(nitProvider=idprovider)
            models.Producto.objects.create(nombreProducto=nombre, precioCompra=precio, 
                                           ivaProducto=iva, stockProducto=cantidad,
                                           nitProveedor = provider)
            return redirect('/admin/')
        else:
            return redirect('/admin/')
    else:
        return redirect('/')
    
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
        return redirect('/')
    
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
        return redirect('/')
            
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
        return redirect('/')

def update_product(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST
            modelo = models.Producto()
            modelo.idProducto = post.get('id')
            modelo.nombreProducto = post.get('nombre')
            modelo.precioCompra = post.get('precio')
            modelo.stockProducto = post.get('cantidad')
            modelo.ivaProducto = float(post.get('iva'))
            idprovider = post.get('provider')
            modelo.nitProveedor = models.Proveedor.objects.get(nitProvider=idprovider)
            modelo.save()
            return redirect('/admin/')
        else:
            return redirect('/admin/')
    else:
        return redirect('/')

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
        return redirect('/')

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
        return redirect('/')

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
        return redirect('/')


def delete_admin(request, id):
    if request.session.get('admin'):
        try:
            admin = models.admin.objects.get(id=id)
            admin.delete()
            return JsonResponse({'mensaje': 'Administrador eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar.'}, status=404)
        
def delete_product(request, id):
    if request.session.get('admin'):
        try:
            admin = models.Producto.objects.get(idProducto=id)
            admin.delete()
            return JsonResponse({'mensaje': 'Producto eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar este producto.'}, status=404)
        
def delete_cashier(request, id):
    if request.session.get('admin'):
        try:
            cajero = models.Cajero.objects.get(idCajero=id)
            cajero.delete()
            return JsonResponse({'mensaje': 'Cajero eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar el cajero.'}, status=404)
        
def delete_provider(request, id):
    if request.session.get('admin'):
        try:
            provider = models.Proveedor.objects.get(nitProvider=id)
            provider.delete()
            return JsonResponse({'mensaje': 'Cajero eliminado correctamente'})
        except models.admin.DoesNotExist:
            return JsonResponse({'error': 'No se pudo eliminar el cajero.'}, status=404)
        
def generate_excel_product(request):
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

    return response
