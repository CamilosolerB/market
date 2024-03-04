from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from . import models

def home_page(request):
    return render(request,'index.html')

def view_provider_page(request):
    queryset = models.Proveedor.objects.all()
    return render(request,'provider.html',{'provider':queryset})

def login_validation(request):
    if request.method == 'POST':
        post = request.POST
        try:
            admin = models.admin.objects.get(email=post.get('email'), password=post.get('password'))
            messages.success(request, '¡Inicio de sesión exitoso!')
            request.session['id'] = admin.id
            return redirect('/home_admin/')     
        except ObjectDoesNotExist:
            try:
                cashier = models.Cajero.objects.get(correo=post.get('email'), password = post.get('password'))
                messages.success(request, '¡Inicio de sesión exitoso!')
                request.session['id'] = cashier.idCashier
                return redirect('/home_client/')
            except ObjectDoesNotExist:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')
                return redirect('/')
    else:
        return redirect('/')

def home_page_admin(request):
    product = models.Producto.objects.all()
    return render(request,'home_admin.html', {'data': product})

def cashier_page(request):
    cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
    return render(request,'home_cash.html', {'data': cashier})

def provider_page(request):
    if request.session.get('id') is not None:
        provider = models.Proveedor.objects.all()
        return render(request, 'provide_mod.html', {'data': provider})

def cerrar_sesion(request):
    request.session['id'] = ''
    return redirect('/')
