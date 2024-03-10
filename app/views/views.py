from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .. import models
from django.contrib.auth.hashers import check_password

def home_page(request):
    return render(request,'index.html')

def login_validation(request):
    if request.method == 'POST':
        post = request.POST
        password = post.get('password')
        try:
            admin = models.admin.objects.get(email=post.get('email'))
            if check_password(password, admin.password):
                messages.success(request, '¡Inicio de sesión exitoso!')
                request.session['id'] = admin.id
                request.session['admin'] = True
                return redirect('/admin/')
            else:
                raise Exception('Contraseña incorrecta')
        except ObjectDoesNotExist:
            try:
                cashier = models.Cajero.objects.get(correo=post.get('email'))
                if check_password(password, cashier.password):
                    messages.success(request, '¡Inicio de sesión exitoso!')
                    request.session['admin'] = False
                    request.session['id'] = cashier.idCashier
                    return redirect('/home_client/')
                else:
                    raise Exception('Contraseña incorrecta')
            except ObjectDoesNotExist:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')
                return redirect('/')
    else:
        return redirect('/')

def cashier_page(request):
    cashier = models.Cajero.objects.get(idCajero = request.session.get('id'))
    return render(request,'home_cash.html', {'data': cashier})

def cerrar_sesion(request):
    request.session['id'] = ''
    request.session['admin'] = False
    return redirect('/')
