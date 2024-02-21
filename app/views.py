from django.shortcuts import render
from .api import proveedorViewSet
from .models import Proveedor
from .serializer import providerSerializer


def view_provider_page(request):
    queryset = Proveedor.objects.all()
    return render(request,'provider.html',{'provider':queryset})