from django import forms
from django.forms import ModelForm
from .models import *

class CategoriaList(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {'nombre' : 'nombre'}
        widgets = {'nombre' : forms.TextInput(attrs={'class':'form-control'})}
class ProductoList(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre',
            'descripcion',
            'precio',
            'imagen',
            'categoria'
        ]
        labels = {
            'id_producto' : 'id_producto',            
            'nombre' : 'nombre',
            'descripcion' : 'descripcion',
            'precio' : 'precio',
            'imagen' : 'imagen',
            'categoria' : 'categoria'
        }
        
        widgets = {
            'id_producto' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.TextInput(attrs={'class':'form-control'}),
            'imagen' : forms.FileInput(attrs={'class':'form-control'}),
            'categoria' : forms.Select(attrs={'class' : 'form-control', 'id' : 'categoria'})
        }    