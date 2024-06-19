from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

