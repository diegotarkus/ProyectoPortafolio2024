from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contacto
from ordenes.models import Orden
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'apellido',
            'correo',
            'mensaje'
        ]
        
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'correo' : 'Correo',
            'mensaje' : 'Mensaje'
        }
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.TextInput(attrs={'class':'form-control'}),
            'mensaje' : forms.TextInput(attrs={'class':'form-control', 'id' : 'mensaje'}),
        }
    