
from django.db import models

class Proveedor(models.Model):
    nit = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    codigoMat = models.CharField(max_length=20, blank=True, null=True)
    nombreProducto = models.CharField(max_length=200, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    unidadMedida = models.CharField(max_length=50, blank=True, null=True)
    unidadCompra = models.CharField(max_length=50, blank=True, null=True)
    unidadMinCompra = models.IntegerField(blank=True, null=True)
    leadTimeDias = models.IntegerField(blank=True, null=True)
    medioTransporte = models.CharField(max_length=50, blank=True, null=True)
    reabastecimiento = models.IntegerField(blank=True, null=True)
    terminoPago = models.CharField(max_length=50, blank=True, null=True)
    tiempoCreditoDias = models.IntegerField(blank=True, null=True)

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    nombreGenerico = models.CharField(max_length=200, blank=True, null=True)
    stockProducto = models.IntegerField(default=0)
    unidadMedida = models.CharField(max_length=50)  
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    cantAdquirida = models.IntegerField(default=0)
    proveedorPrincipal = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, related_name='principal', null=True, blank=True
    )
    proveedorSuplente = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, related_name='suplente', null=True, blank=True
    )
    proveedor3 = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, related_name='proveedor3', null=True, blank=True
    )
    proveedor4 = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, related_name='proveedor4', null=True, blank=True
    )

    def __str__(self):
        return self.nombreProducto


class StorageItem(models.Model):
    idItem = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.item_name} ({self.quantity})"
    

class Bodega(models.Model):
    ubicacion = models.CharField(max_length=50)
    nivel = models.IntegerField()
    posicion = models.IntegerField()
    localizador = models.CharField(max_length=20)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    unidad = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

class Cliente(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True, default='00001')
    nombre = models.CharField(max_length=200, default='Nombre Cliente')
    razon_social = models.CharField(max_length=200, default='Razón Social Cliente')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    tipo_agua = models.CharField(max_length=100, blank=True, null=True)
    cantidad_promedio_kg = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Usuario(models.Model):
    idCajero = models.AutoField(primary_key=True)
    nombreCajero = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    salario = models.FloatField(default=0)
    totalEarning = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombreCajero} - {self.correo}"


class admin(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)

class stats(models.Model):
    id = models.IntegerField(primary_key=True)
    sellsOneWeek = models.FloatField(max_length=11)
    sellsTwoWeek = models.FloatField(max_length=11)
    sellsThreeWeek = models.FloatField(max_length=11)
    sellsFourWeek = models.FloatField(max_length=11)
    nequi = models.CharField(max_length=255)
    daviplata = models.CharField(max_length=255)
    