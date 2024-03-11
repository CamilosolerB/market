from django.urls import path
from ..views import view_cashier

urlpatterns = [
    path('', view_cashier.cashier_page),
]