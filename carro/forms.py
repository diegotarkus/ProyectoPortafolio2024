from django import forms

cantidades_producto = [(i, str(i)) for i in range (1, 21)]

class anadirProductoForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=cantidades_producto, coerce=int)
    update = forms.BooleanField(required=False, initial= False, widget=forms.HiddenInput)