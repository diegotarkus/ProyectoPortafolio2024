from django import forms
from .models import Orden

class OrdenForm (forms.ModelForm):
    class Meta:
        model = Orden
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'comuna',
            'ciudad',
            'comentario',
            
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido' : 'Apellido',
            'direccion' : 'Direccion',
            'telefono' : 'Telefono',
            'comuna' : 'Comuna',
            'ciudad' : 'Ciudad',
            'comentario' : 'Comentario',
            'cupon' : 'cupon',
            'descuento' : 'descuento',
            'total_oc' : 'total_oc',
            'user' : 'user'
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
            'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class' : 'form-control'}),
            'comuna' : forms.TextInput(attrs={'class' : 'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class' : 'form-control'}),
            'comentario' : forms.TextInput(attrs={'class' : 'form-control'}),
            'cupon' : forms.TextInput(attrs={'is_hidden' : True}),
            'descuento' : forms.TextInput(attrs={'is_hidden' : True}),
            'total_oc' : forms.TextInput(attrs={'is_hidden' : True}),
            'user' : forms.TextInput(attrs={'is_hidden' : True})
        }
        
class OrdenFormAdmin(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['estado']
        labels = {'estado' : 'estado'}
        widgets = {'estado' : forms.Select(attrs={'class' : 'form-control'})}
        