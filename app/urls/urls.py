# app/urls/urls.py
from django.urls import path
from ..views import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('login/', views.login_validation, name='login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
