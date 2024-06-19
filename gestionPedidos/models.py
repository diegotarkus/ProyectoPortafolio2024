from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id_producto=models.CharField(primary_key=True, verbose_name='id_producto')
    nombre=models.CharField(max_length=100, verbose_name='nombre')
    descripcion=models.CharField(max_length=500, verbose_name='descripcion', null=True, blank=True)
    precio=models.IntegerField(verbose_name='precio')
    imagen=models.ImageField(verbose_name='imagen', upload_to='productos', null=True, blank=True)
    categoria=models.ForeignKey(Categoria, verbose_name='categoria', on_delete=models.CASCADE)

    def __str__(self):
        return (self.nombre)
    
    def get_absolute_url(self):
        return reverse("detalle_producto", args=[self.id_producto])




