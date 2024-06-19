from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from gestionPedidos.models import Producto, Categoria
from .forms import *

@staff_member_required
def categoria_nuevo(request):
    if request.method == 'POST':
        form = CategoriaList(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            obj = Categoria.objects.create(
                nombre = nombre
            )
            obj.save()
            return redirect(reverse('productos'))
        else:
            return redirect(reverse('home'))
    else:
        form = CategoriaList
    return render(request, 'categoria_nuevo.html', {'form' : form})

@staff_member_required
def producto_nuevo(request):
    if request.method == 'POST' :
        form = ProductoList(request.POST, request.FILES)
        if form.is_valid():
            id_producto = form.cleaned_data.get('id_producto')
            nombre = form.cleaned_data.get('nombre')
            descripcion = form.cleaned_data.get('descripcion')
            precio = form.cleaned_data.get('precio')
            imagen = form.cleaned_data.get('imagen')
            categoria = form.cleaned_data.get('categoria')
            obj = Producto.objects.create(
                id_producto = id_producto,
                nombre = nombre,
                descripcion = descripcion,
                precio = precio,
                imagen = imagen,
                categoria = categoria
            )
            obj.save()
            return redirect (reverse('productos'))
        else:
            return redirect (reverse('home'))
    else:
        form = ProductoList    
    return render(request, "producto_nuevo.html", {'form' : form})

@staff_member_required
def producto_editar(request, id_producto):
    try:
        producto = Producto.objects.get(id_producto = id_producto)
        form = ProductoList(instance = producto)

        if request.method == 'POST':
            form = ProductoList(request.POST, request.FILES, instance = producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('productos') + '?UPDATED')
            else:
                return redirect(reverse('producto_editar') + id_producto) 

        context = {'form' : form}
        return render(request,'producto_editar.html', context)
    except:
        return redirect(reverse('productos') + '?NO_EXISTS')
    
@staff_member_required   
def producto_borrar(request, id_producto):
    try:
        producto = Producto.objects.get(id_producto = id_producto)
        producto.delete()
        return redirect(reverse('productos') + '?DELETED')
    except:
        return redirect(reverse('productos') + '?FAIL')

@staff_member_required
def lista_productos(request):
    context = {'productos': Producto.objects.all()}
    return render(request,'productos.html', context)