
from django import forms
from app.models import Cliente


TIPO_USUARIO = [
    ('admin', 'Administrador'),
]   

class RegistroUsuarioForm(forms.Form):
    tipo = forms.ChoiceField(choices=TIPO_USUARIO, label='Tipo de usuario')
    nombre = forms.CharField(max_length=100, label='Nombre')
    correo = forms.EmailField(max_length=100, label='Correo electrónico')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

TIPO_AGUA = [
    ('POZO SEPTICO', 'Pozo Séptico'),
    ('RED PÚBLICA', 'Red Pública'),
]

class ClienteForm(forms.Form):
    codigo = forms.CharField(max_length=10, label='Código')
    nombre_cliente = forms.CharField(max_length=200, label='Cliente')
    razon_social = forms.CharField(max_length=200, label='Razón Social')
    telefono = forms.CharField(max_length=15, label='Teléfono')
    contacto = forms.CharField(max_length=100, label='Contacto', required=False)
    correo = forms.EmailField(max_length=100, label='Correo')
    ciudad = forms.CharField(max_length=100, label='Ciudad', required=False)
    tipo_agua = forms.ChoiceField(choices=TIPO_AGUA, label='Tipo de Agua')
    cantidad_promedio_kg = forms.FloatField(label='Cantidad Promedio KG', required=False)