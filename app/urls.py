from django.urls import path
from .views import view_provider_page

urlpatterns = [
    path('provider/', view_provider_page, name="lista_productos")
]