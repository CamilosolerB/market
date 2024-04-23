from django.urls import path
from ..views import views_cashier

urlpatterns = [
    path('', views_cashier.cashier_page),
    path('products/',views_cashier.inventory_page),
    path('search_product/', views_cashier.get_product),
    path('create_sale/', views_cashier.finish_shop),
    path('search_client/', views_cashier.search_client),
]