from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .. import models
from django.contrib.auth.hashers import check_password, make_password

def home_page(request):
    return render(request,'index.html')

def login_validation(request):
    if request.method == 'POST':
        post = request.POST
        password = post.get('password')
        try:
            admin = models.admin.objects.get(email=post.get('email'))
            if check_password(password, admin.password):
                request.session['id'] = admin.id
                request.session['admin'] = True
                messages.success(request, '¡Inicio de sesión exitoso!')
                return redirect('/admin/')
            else:
                messages.error(request, 'Contraseña incorrecta')
        except models.admin.DoesNotExist:
            try:
                cashier = models.Cajero.objects.get(correo=post.get('email'))
                if check_password(password, cashier.password):
                    request.session['id'] = cashier.idCajero
                    request.session['cajero'] = True
                    messages.success(request, '¡Inicio de sesión exitoso!')
                    return redirect('/cashier/')
                else:
                    messages.error(request, 'Contraseña incorrecta')
                    raise ValueError('Contraseña incorrecta')
            except models.Cajero.DoesNotExist:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')
                return redirect('/')
    else:
        return redirect('/')

def cerrar_sesion(request):
    request.session['id'] = ''
    request.session['admin'] = False
    request.session['cajero'] = False
    return redirect('/')
