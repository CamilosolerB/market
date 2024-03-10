from django.urls import path
from ..views import views

urlpatterns = [
    path('',views.home_page, name="index"),
    path('home_client/',views.cashier_page, name="page_client"),
    path('login/',views.login_validation, name="login"),
    path('singout/',views.cerrar_sesion, name="singout")
]
