from django import forms
from django.forms import ModelForm
from .models import *

class ProductoList(ModelForm):
    
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'precio',
            'imagen'
        ]
        labels = {
            'id_producto' : 'id_producto',            
            'nombre' : 'nombre',
            'precio' : 'precio',
            'imagen' : 'imagen'
        }
        widgets = {
            'id_producto' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'}),
        }    