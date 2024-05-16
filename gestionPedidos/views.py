from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import HttpResponse
from gestionPedidos.models import Producto
from .forms import *

# Create your views here.

def producto_nuevo(request):
    if request.method == 'POST' :
        form = ProductoList(request.POST, request.FILES)
        if form.is_valid():
            id_producto = form.cleaned_data.get('id_producto')
            nombre = form.cleaned_data.get('nombre')
            precio = form.cleaned_data.get('precio')
            imagen = form.cleaned_data.get('imagen')
            obj = Producto.objects.create(
                id_producto = id_producto,
                nombre = nombre,
                precio = precio,
                imagen = imagen
            )
            obj.save()
            return redirect (reverse('producto_nuevo/'))
    else:
        form = ProductoList    
    return render(request, "producto_nuevo.html", {'form' : form})

def lista_productos(request):
    context = {'productos': Producto.objects.all()}
    return render(request,'productos.html',context)