from django.urls import path
from ..views import views

urlpatterns = [
    path('',views.home_page, name="index"),
    path('login/',views.login_validation, name="login"),
    path('singout/',views.cerrar_sesion, name="singout")
]
