# app/views/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .. import models
from ..forms import RegistroUsuarioForm  # Asegúrate de que exista

# 🔹 Página de inicio
def home_page(request):
    return render(request, 'index.html')


# 🔹 Registro de usuarios
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            password = make_password(form.cleaned_data['password'])

            if tipo == 'admin':
                if models.admin.objects.filter(email=correo).exists():
                    messages.error(request, 'Ya existe un administrador con ese correo.')
                else:
                    models.admin.objects.create(email=correo, password=password)
                    messages.success(request, '¡Administrador registrado exitosamente!')
                    return redirect('login')

            # Si quisieras habilitar cajero, descomenta y asegúrate de que exista el modelo
            """
            elif tipo == 'cajero':
                if models.Cajero.objects.filter(correo=correo).exists():
                    messages.error(request, 'Ya existe un cajero con ese correo.')
                else:
                    salario = form.cleaned_data.get('salario', 0)
                    totalEarning = form.cleaned_data.get('totalEarning', 0)
                    models.Cajero.objects.create(
                        nombreCajero=nombre,
                        salario=salario,
                        correo=correo,
                        password=password,
                        totalEarning=totalEarning
                    )
                    messages.success(request, '¡Cajero registrado exitosamente!')
                    return redirect('login')
            """
        else:
            messages.error(request, 'Error en el formulario. Verifica los campos.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})


# 🔹 Login
def login_validation(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar si es admin
        try:
            admin = models.admin.objects.get(email=email)
            if check_password(password, admin.password):
                request.session['id'] = admin.id
                request.session['admin'] = True
                messages.success(request, '¡Inicio de sesión exitoso como administrador!')
                return redirect('/admin/')
            else:
                messages.error(request, 'Contraseña incorrecta para administrador.')
        except models.admin.DoesNotExist:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')

        # Cajero comentado temporalmente
        """
        try:
            cajero = models.Cajero.objects.get(correo=email)
            if check_password(password, cajero.password):
                request.session['id'] = cajero.idCajero
                request.session['cajero'] = True
                messages.success(request, '¡Inicio de sesión exitoso como cajero!')
                return redirect('/cashier/')
            else:
                messages.error(request, 'Contraseña incorrecta para cajero.')
        except models.Cajero.DoesNotExist:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
        """

    return render(request, 'index.html')


# 🔹 Cerrar sesión
def cerrar_sesion(request):
    request.session.flush()
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('login')
