from django.db import models
import re
from django.contrib.auth import get_user_model

User = get_user_model()
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
class Contacto(models.Model):
    nombre=models.CharField(max_length=30, verbose_name="nombre")
    apellido=models.CharField(max_length=30, verbose_name="apellido")
    correo=models.EmailField(verbose_name="correo")
    mensaje = models.TextField(verbose_name='mensaje', max_length=500)
    creado = models.DateTimeField(verbose_name='creado', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return (self.creado)
    