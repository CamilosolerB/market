from rest_framework import serializers
from .models import Proveedor, Producto, Cliente, Cajero, Factura, Compra

class providerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('nitProvider','nomProvider')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto','nombreProducto', 'precioCompra','ivaProducto','stock', 'nitProveedor')

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('cedula','nombreCliente','numeroCompras','correo','telefono')

class cajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cajero
        fields = ('nitProvider','nomProvider')

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('idFactura','cedulaCliente','idCajero','totalBruto','totalIva','subtotal','day')
        read_only_fields = ('day')

class facturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('idCompra','idProducto','cantidad','total','utilidad','idFactura')
        read_only_fields = ('day')
