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
            return redirect('/home_admin/')
            request.session['token'] = post.get('token')
        except ObjectDoesNotExist:
            try:
                cashier = models.Cajero.objects.get(correo=post.get('email'), password = post.get('password'))
                messages.success(request, '¡Inicio de sesión exitoso!')
                return redirect('/home_client/')
                request.session['token'] = post.get('token')
            except ObjectDoesNotExist:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')
                return redirect('/')
    else:
        return redirect('/')

def home_page_admin(request):
    return render(request,'home_admin.html')

def cashier_page(request):
    return render(request,'home_cash.html')

def cerrar_sesion(request):
    request.session['token'] = ''
    return redirect('/')