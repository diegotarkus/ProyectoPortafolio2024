from django import forms

class CuponForm(forms.Form):
    codigo = forms.CharField()
