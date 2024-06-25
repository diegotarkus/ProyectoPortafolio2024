from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from guest_user.decorators import allow_guest_user
from django.db.models import Q
from .models import *
from gestionPedidos.models import Producto, Categoria
from .forms import *
from carro.forms import anadirProductoForm
import bcrypt

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    context = {'productos': Producto.objects.all()}
    return render(request, "home.html", context)

def lista_categoria(request, id):
    busqueda = request.POST.get("buscador")
    lista_productos = Producto.objects.filter(categoria=id)
    
    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__icontains=busqueda),
            Q(descripcion__icontains=busqueda)
        ).distinct()
    
    context = {'lista_productos' : lista_productos}
    return render(request, 'home', context)


def detalle_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    form = anadirProductoForm()
    return render(request, 'productos/detalle_producto.html', {'producto': producto, 'form': form})
    
def registrar(request):
    data = {'form' : RegistroForm()}
    if request.method == 'POST':
        formulario = RegistroForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(usermame = formulario.cleaned_data['username'], password = formulario.cleaned_data['password1'])
            if user is not None:
                login(request, user)
            messages.success(request, 'Usuario registrado satisfactoriamente.')
            return redirect('/')
        else:
            data['form'] = formulario
    return render(request, 'auth/registrar.html', data)

    
def exit(request):
    logout(request)
    return redirect('home')
