from django.urls import path
from . import views

urlpatterns = [
    path('provider/', views.view_provider_page, name="lista_productos"),
    path('',views.home_page, name="index"),
    path('home_admin/', views.home_page_admin, name="index_admin"),
    path('home_client/',views.cashier_page, name="page_client"),
    path('login/',views.login_validation, name="login"),
    path('singout/',views.cerrar_sesion, name="singout")
]
