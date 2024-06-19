from django.db import models
from gestionPedidos.models import Producto
from django.contrib.auth import get_user_model

User = get_user_model()

class Orden (models.Model):
    class Estado (models.TextChoices):
        PENDIENTE = "PENDIENTE"
        COMPLETADA = "COMPLETADA"
        CANCELADA = "CANCELADA"
    
    nombre = models.TextField(max_length=30, verbose_name="nombre")
    apellido = models.TextField(max_length=50, verbose_name="apellido")
    direccion = models.TextField(max_length=200, verbose_name="direccion")
    comuna = models.TextField(max_length=50, verbose_name="comuna")
    ciudad = models.TextField(max_length=50, verbose_name="ciudad")
    telefono = models.TextField(max_length=12, verbose_name="telefono", default=0)
    comentario = models.TextField(max_length=500, verbose_name="comentario", blank=True)
    creada = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.PENDIENTE)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= "Orden"
        verbose_name_plural = "Ordenes"
        
    def __str__(self):
        return 'Orden #{}'.format(self.id)
    
class OrdenItem (models.Model):
    orden = models.ForeignKey(Orden, verbose_name="orden", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name="orden_productos", on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name="precio")
    cantidad = models.IntegerField(verbose_name="cantidad")
    
    def __str__(self):
        return 'Orden #{}'.format(self.orden.id)
    
    



