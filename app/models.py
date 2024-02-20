from django.db import models

class Proveedor(models.Model):
    nitProvider = models.IntegerField(primary_key=True)
    nomProvider = models.CharField(max_length=50)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    precioCompra = models.FloatField(null=True)
    ivaProducto = models.FloatField(null=True)
    stockProducto = models.IntegerField(null=True)
    nitProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Cliente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombreCliente = models.CharField(max_length=100)
    numeroCompras = models.IntegerField(max_length=3)
    correo = models.CharField(max_length=100)
    telefono = models.FloatField(max_length=11)

class Cajero(models.Model):
    idCajero = models.IntegerField(primary_key=True)
    nombreCajero = models.CharField(max_length=100)
    salario = models.FloatField(max_length=11)

class Factura(models.Model):
    idFactura = models.IntegerField(primary_key=True)
    cedulaCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idCajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)
    totalBruto = models.FloatField(null=False)
    totalIva = models.FloatField(null=False)
    subTotal = models.FloatField(null=False)
    day = models.DateTimeField(auto_now_add=True)

class Compra(models.Model):
    idCompra = models.IntegerField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    total = models.FloatField(null=False)
    utilidad = models.FloatField(null=False)
    idFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)