from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

cantidades_producto = [(i, str(i)) for i in range (1, 21)]

class anadirProductoForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=cantidades_producto, coerce=int)