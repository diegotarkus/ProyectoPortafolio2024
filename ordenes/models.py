from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from gestionPedidos.models import Producto
from cupones.models import Cupon
from django.contrib.auth import get_user_model

User = get_user_model()

class Orden (models.Model):
    class Estado (models.TextChoices):
        PENDIENTE = "PENDIENTE"
        EN_PREPARACION = "EN PREPARACIÓN"
        COMPLETADA = "COMPLETADA"
        CANCELADA = "CANCELADA"
    
    nombre = models.CharField(max_length=30, verbose_name="nombre")
    apellido = models.CharField(max_length=50, verbose_name="apellido")
    direccion = models.CharField(max_length=200, verbose_name="direccion")
    comuna = models.CharField(max_length=50, verbose_name="comuna")
    ciudad = models.CharField(max_length=50, verbose_name="ciudad")
    telefono = models.CharField(max_length=12, verbose_name="telefono", default=0)
    comentario = models.CharField(max_length=500, verbose_name="comentario", blank=True)
    cupon = models.ForeignKey(Cupon, verbose_name="cupon", on_delete=models.CASCADE, blank=True, null=True, default=False)
    subtotal = models.IntegerField(verbose_name="subtotal")
    descuento = models.IntegerField(verbose_name="descuento", default=0, blank=True)
    total_oc = models.IntegerField(verbose_name="total_oc", default=0)
    creada = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= "Orden"
        verbose_name_plural = "Ordenes"
        get_latest_by = "id"
        
    def __str__(self):
        return 'Orden #{}'.format(self.id)
    
    def valor_total(self):
        valor_total = self.sub_total() - self.descuento()
        return valor_total
        
    def total(self):
        subtotal = sum(item.total_item() for item in self.items.all())
        total = subtotal - subtotal*(self.descuento / Decimal('100'))
        return total
    
class OrdenItem (models.Model):
    orden = models.ForeignKey(Orden, verbose_name="orden", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name="orden_productos", on_delete=models.CASCADE)
    precio = models.IntegerField(verbose_name="precio")
    cantidad = models.IntegerField(verbose_name="cantidad")
    
    def __str__(self):
        return 'Orden #{}'.format(self.orden.id)
    
    def total_item(self):
        total_item = self.precio * self.cantidad
        return total_item
    
class Transaccion (models.Model):
    orden = models.ForeignKey(Orden, verbose_name="orden", on_delete=models.CASCADE)
    vci = models.CharField(max_length=5, verbose_name="VCI")
    status = models.CharField(max_length=65, verbose_name="status")
    buy_order = models.CharField(max_length=27, verbose_name="num_trans")
    session_id = models.CharField(max_length=62, verbose_name="id_session")
    card_number = models.CharField(verbose_name="num_tarjeta")
    accounting_date = models.CharField(max_length=4, verbose_name="fecha_auth")
    transaction_date = models.CharField(verbose_name="fecha_trans", null=True)
    authorization_code = models.CharField(max_length=7, verbose_name="cod_auth")
    payment_type_code = models.CharField(max_length=3, verbose_name="tipo_pago")
    response_code = models.CharField(max_length=3, verbose_name="cod_respuesta")
    installments_number = models.CharField(max_length=3, verbose_name="num_cuotas")
    
    class Meta:
        verbose_name= "Transacción"
        verbose_name_plural = "Transacciones"
        
    def __str__(self):
        return (self.accounting_date)

    

    
    



