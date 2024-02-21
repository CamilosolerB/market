from .models import Proveedor
from rest_framework import viewsets, permissions
from .serializer import providerSerializer

def returnProvider():
    return 


class proveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = providerSerializer
        