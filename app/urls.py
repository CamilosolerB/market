from django.urls import path
from . import views

urlpatterns = [
    path('provider/', views.view_provider_page, name="lista_productos"),
    path('',views.home_page, name="index"),
    path('home_admin/', views.home_page_admin, name="index_admin"),
]
