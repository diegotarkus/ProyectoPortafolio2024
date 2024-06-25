from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cupon(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    valido_hasta = models.DateTimeField()
    descuento = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    activo = models.BooleanField()
    
    def __str__(self):
        return self.codigo
    
