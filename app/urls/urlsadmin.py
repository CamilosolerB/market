from django.urls import path
from ..views import view_admin

urlpatterns = [
    path('', view_admin.home_page_admin),
    path('providers/', view_admin.provider_page),
    path('cashiers/', view_admin.cashier_admin),
    path('admins/', view_admin.admin_interface),
    path('create_product/', view_admin.create_product),
    path('create_admin/', view_admin.create_admin),
    path('create_cashier/', view_admin.create_cashier),
    path('create_provider/', view_admin.create_provider),
    path('update_product/',view_admin.update_product),
    path('update_admin/',view_admin.update_admin),
    path('update_cashier/',view_admin.update_cashier),
    path('update_provider/',view_admin.update_provider),
    path('delete_product/<int:id>', view_admin.delete_product),
    path('delete_admin/<int:id>', view_admin.delete_admin),
    path('delete_cashier/<int:id>', view_admin.delete_cashier),
    path('delete_provider/<int:id>', view_admin.delete_provider),
    path('qrpage/',view_admin.qr_admin),
    path('qrpage/nequi/',view_admin.create_nequi_qr),
    path('qrpage/daviplata/',view_admin.create_nequi_qr),
    path('generate_excel/',view_admin.generate_excel_product)
]