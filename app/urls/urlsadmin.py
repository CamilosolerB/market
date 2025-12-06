from django.urls import path
from ..views import view_admin

urlpatterns = [
    path('', view_admin.home_page_admin),
    path('providers/', view_admin.provider_page),
    path('storage/', view_admin.storage_page, name='storage_page'),
    path('admins/', view_admin.admin_interface),
    path('bodega/', view_admin.bodega_page, name='bodega_page'),
    path('clientes/', view_admin.clientes_page, name='clientes_page'),
    
    path('create_cliente/', view_admin.create_cliente, name='create_cliente'),
    path('create_bodega/', view_admin.create_bodega, name='create_bodega'),
    path('create_product/', view_admin.create_product),
    path('create_admin/', view_admin.create_admin),
    path('create_storage_item/', view_admin.create_storage_item, name='create_storage_item'),
    path('create_provider/', view_admin.create_provider),
    
    
    path('update_storage_item/', view_admin.update_storage_item, name='update_storage_item'),
    path('update_product/',view_admin.update_product),
    path('update_admin/',view_admin.update_admin),
    path('update_provider/',view_admin.update_provider),
    path('update_bodega/<int:id>/', view_admin.update_bodega, name='update_bodega'),
    path('update_cliente/<str:codigo>/', view_admin.update_cliente, name='update_cliente'),
    
    
    path('delete_cliente/<str:codigo>/', view_admin.delete_cliente, name='delete_cliente'),
    path('delete_bodega/<int:id>/', view_admin.delete_bodega, name='delete_bodega'),
    path('delete_product/<int:id>', view_admin.delete_product),
    path('delete_admin/<int:id>', view_admin.delete_admin),
    path('delete_storage_item/<int:id>/', view_admin.delete_storage_item, name='delete_storage_item'),
    path('delete_provider/<int:id>', view_admin.delete_provider),
    
    path('qrpage/',view_admin.qr_admin),
    path('qrpage/nequi/',view_admin.create_nequi_qr),
    path('qrpage/daviplata/',view_admin.create_daviplata_qr),
    path('generate_excel/',view_admin.generate_excel_product),
    path('generate_pdf/',view_admin.generate_pdf_product),

    path("importar/", view_admin.importar_excel, name="importar_excel"),
    path('general/', view_admin.vista_general, name='vista_general'),


]