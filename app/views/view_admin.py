from django.shortcuts import render, redirect
from .. import models
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

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
            iva = float(post.get('iva')) / 100
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
            admin = models.admin.objects.create(email=email)
            clave = make_password(password)
            admin.password = clave
            admin.save()
            return redirect('/admin/admins')
        else:
            return redirect('/admin/')
    else:
        return redirect('/')
    
def create_cashier(request):
    if request.session.get('admin'):
        if request.method == 'POST':
            post = request.POST

    
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