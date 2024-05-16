from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut=models.CharField(primary_key=True, max_length=10, verbose_name="RUT")
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    correo=models.EmailField()
    telefono=models.CharField(max_length=9, verbose_name="Teléfono")
    direccion=models.CharField(max_length=20, verbose_name="Dirección")

    def __str__(self):
        return (self.correo)
    
class Pedido(models.Model):
    id_pedido=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    precio=models.IntegerField()
    nota=models.CharField(max_length=255, blank=True, null=True)
    estado=models.CharField(max_length=255, null=True)

    def __str__(self):
        return (self.id_pedido)
    
####    Clase que se utilizará para poder aplicar descuentos en los pedidos    ####
class Descuento(models.Model):
    id_descuento=models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return (self.id_descuento)

####    Clase que se utilizará para verificar el estado de un producto (recibido, proceso, reparto y entregado)    ####
class Estado(models.Model):
    id_estado=models.IntegerField(primary_key=True)
    descripcion=models.CharField(max_length=255)

    def __str__(self):
        return (self.id_estado)