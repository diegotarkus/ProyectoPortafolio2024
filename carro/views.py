from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from gestionPedidos.models import Producto
from .carro import Carro
from .forms import anadirProductoForm
from cupones.forms import CuponForm

@require_POST
def carro_mas(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=id_producto)
    form = anadirProductoForm(request.POST)
    if form.is_valid():
        carro.anadir(
            producto=producto,
            cantidad=form.cleaned_data['cantidad'],
            update=form.cleaned_data['update'])
    return redirect('carro:detalle_carro')


    
def carro_menos(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carro.eliminar(producto=producto)
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

def detalle_carro(request):
    carro = Carro(request)
    for item in carro:
        item['update_cantidad_form'] = anadirProductoForm(initial={'cantidad': item['cantidad'], 'update': True})
    return render(request, 'detalle_carro.html', {'carro': carro})
