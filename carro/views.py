from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from gestionPedidos.models import Producto
from .carro import Carro
from .forms import anadirProductoForm
from guest_user.decorators import allow_guest_user
#aqui va el form cupon

def carro_mas(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carro.anadir(producto=producto)
    return redirect('carro:detalle_carro')

def carro_menos(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carro.remover(producto=producto)
    return redirect('carro:detalle_carro')

def carro_eliminar(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carro.eliminar(producto=producto)
    return redirect('carro:detalle_carro')

def carro_limpiar(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect('/')

@allow_guest_user
def detalle_carro(request):
    carro = Carro(request)
    return render(request, 'detalle_carro.html', {'carro': request.session['carro']})
