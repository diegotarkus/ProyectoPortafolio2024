from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z.]+$')
        PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')
    
        errors = {}
    
        if len(Cliente.objects.filter(correo=postData['correo'])) > 0:
           errors['correo_exits'] = "Correo ya existente."
    
        else:
            if len(postData['nombre'].strip()) < 2 or len(postData['nombre'].strip()) > 40:
                errors['nombre_len'] = "Nombre debe tener entre 2 y 40 caracteres"
            if len(postData['apellido'].strip()) < 2 or len(postData['apellido'].strip()) > 40:
                 errors['apellido_len'] = "Apellido debe tener entre 2 y 40 caracteres"
            
        if not SOLO_LETRAS.match(postData['nombre']) or not SOLO_LETRAS.match(postData['apellido']):
            errors['solo_letras']  = "Favor ingresar solo letras."
        
        if not EMAIL_REGEX.match(postData['correo']):
            errors['correo'] = "Correo no válido."
            
        if not PASSWORD_REGEX.match(postData['password']):
            errors['password_format'] = "Formato de contraseña no válido"
            
        if postData['password'] != postData['password_confirm']:
            errors['password_confirm'] = "Contraseñas no coinciden"

        return errors
class Cliente(models.Model):
    rut=models.CharField(primary_key=True, max_length=10, verbose_name="RUT")
    nombre=models.CharField(max_length=15, verbose_name="nombre")
    apellido=models.CharField(max_length=15, verbose_name="apellido")
    correo=models.EmailField(verbose_name="correo")
    telefono=models.CharField(max_length=9, verbose_name="telefono")
    direccion=models.CharField(max_length=20, verbose_name="direccion")
    password = models.CharField(verbose_name='password', max_length=500, default='nopass')
    password_decode = models.CharField(verbose_name='Password_Hash', max_length=500)
    rol = models.CharField(verbose_name='rol', max_length=20, default='USER')
    creado = models.DateTimeField(verbose_name='creado', auto_now_add=True, null=True, blank=True)
    objects = UserManager()

    def __str__(self):
        return (self.rut)
    
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