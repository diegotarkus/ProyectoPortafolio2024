from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from guest_user.decorators import allow_guest_user
from django.db.models import Q
from .models import *
from gestionPedidos.models import Producto, Categoria
from ordenes.models import Orden, OrdenItem
from .forms import *
from carro.forms import anadirProductoForm
import bcrypt


def root(request):
    return redirect('/home')

@allow_guest_user
def home(request):
    context = {'productos': Producto.objects.all(), 'categoria' : Categoria.objects.all(), 'orden' : Orden.objects.all()}
    return render(request, "home.html", context)

def categoria(request, foo):
    foo = foo.replace('-', ' ')
    categoria = Categoria.objects.get(nombre=foo)
    print(categoria)
    productos = Producto.objects.filter(categoria=categoria)
    print(productos)
    return render(request, 'categoria.html', {'productos' : productos, 'categoria' : categoria })

def busca_ordenes(request):
    if request.method == 'POST':
        miorden = request.POST['miorden']
        try:
            orden = Orden.objects.get(id=miorden)
            items = OrdenItem.objects.filter(orden=miorden)
            print(miorden, orden, items)
            return render(request, 'buscaordenes.html', {'miorden' : miorden, 'orden':orden, 'items' : items})
        except:
            return redirect(reverse('busca-ordenes')+ '?NO_EXISTS')
    else:
        return render(request, 'buscaordenes.html')
    

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            correo = form.cleaned_data.get('correo')
            mensaje = form.cleaned_data.get('mensaje')
            obj = Contacto.objects.create(
                nombre = nombre,
                apellido = apellido,
                correo = correo,
                mensaje = mensaje
            )
            obj.save()
            return redirect(reverse('home')+ '?OK')
        else:
            return redirect(reverse('contacto')+ '?FAIL')
    else:
        form = ContactoForm
    return render(request,'contacto.html',{'form':form})

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
