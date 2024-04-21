from django.urls import path
from ..views import view_cashier

urlpatterns = [
    path('', view_cashier.cashier_page),
    path('products/',view_cashier.inventory_page),
    path('search_product/', view_cashier.get_product),
    path('create_sale/', view_cashier.finish_shop),
    path('search_client/', view_cashier.search_client),
]