from django.db import models


# Create your models here.

####    MODELO DE DATOS    ####


class Producto(models.Model):
    id_producto=models.IntegerField(primary_key=True, verbose_name='id_producto')
    nombre=models.CharField(max_length=20, verbose_name='nombre')
    precio=models.IntegerField(verbose_name='precio')
    imagen=models.ImageField(verbose_name='imagen', upload_to='productos', null=True, blank=True)

    def __str__(self):
        return (self.nombre)




