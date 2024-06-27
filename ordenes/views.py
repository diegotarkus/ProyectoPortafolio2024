from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from guest_user.decorators import allow_guest_user
from .forms import OrdenForm, OrdenFormAdmin
from cupones.models import Cupon
from cupones.forms import CuponForm
from .models import Orden, OrdenItem
from gestionPedidos.models import Producto
from carro.carro import Carro

User = get_user_model()

@allow_guest_user
def orden_nuevo(request):
    carro = Carro(request)
    usuario = User.objects.get(username=request.user.username)
    subtotal = carro.carro_total()
    total = carro.total()
    if carro.cupon:
        cupon = carro.cupon
        descuento = carro.descuento()
        desc = Cupon.desc(cupon)
        print("desc:", desc)
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            direccion = form.cleaned_data.get('direccion')
            comuna = form.cleaned_data.get('comuna')
            ciudad = form.cleaned_data.get('ciudad')
            telefono = form.cleaned_data.get('telefono')
            comentario = form.cleaned_data.get('comentario')
            subtotal = subtotal
            cupon = cupon
            descuento = descuento
            total_oc = total
            user = usuario
            orden = Orden.objects.create(
                nombre = nombre,
                apellido = apellido,
                direccion = direccion,
                comuna = comuna,
                ciudad = ciudad,
                telefono = telefono,
                comentario = comentario,
                subtotal = subtotal,
                cupon = cupon,
                descuento = descuento,
                total_oc = total_oc,
                user = user
            )            
            orden.save()
                     
            for item in carro:
                OrdenItem.objects.create(
                    orden = orden,
                    producto = item['producto'],
                    precio = item['precio'],
                    cantidad = item['cantidad']
                )
            carro.limpiar()
        return render(request, 'exito.html', {'orden' : orden})
    else:
        form = OrdenForm()
        cuponform = CuponForm()
    context = {'carro' : carro, 'form' : form, 'cuponform' : CuponForm}
    return render(request, 'checkout.html', context)

@staff_member_required
def ordenes_lista(request):
    form = OrdenFormAdmin()
    if request.method == 'POST':
        form = OrdenFormAdmin(request.POST)
        if form.is_valid():
            estado = form.cleaned_data.get('estado')
            Orden.objects.update(estado=estado)
        else:
            form = OrdenFormAdmin
            
    context = {'ordenes' : Orden.objects.all(), 'form' : form}
    return render(request,'admin/ordenlist.html',context)
   
        

@staff_member_required
def orden_editar(request, id):
    try:
        orden = Orden.objects.get(id = id)
        ordenForm = OrdenForm(instance = orden)
        items = OrdenItem.objects.filter(orden=id)
        if request.method == 'POST':
            ordenForm = OrdenForm(request.POST, instance = orden)
            if ordenForm.is_valid():
                ordenForm.save()
                return redirect(reverse('ordenes:ordenes_lista') + '?UPDATED')
            else:
                return redirect(reverse('ordenes:orden_editar') + id_producto) 

        context = {'orden' : orden, 'ordenForm' : ordenForm, 'items' : items}
        return render(request,'admin/orden_editar.html', context)
    except:
        return redirect(reverse('ordenes:ordenes_lista') + '?NO_EXISTS')
    
def orden_estado(request, id):
    try:
        orden = Orden.objects.get(id = id)
        form = OrdenFormAdmin(instance = orden)
        if request.method == 'POST':
            form = OrdenFormAdmin(request.POST, instance = orden)
            if form.is_valid():
                form.save()
                return redirect(reverse('ordenes:ordenes_lista') + '?UPDATED')
            else:
                return redirect(reverse('ordenes:orden_editar') + id_producto) 

        context = {'form' : form}
        return render(request,'orden_editar.html', context)
    except:
        return redirect(reverse('ordenes:ordenes_lista') + '?NO_EXISTS')    
    
@staff_member_required   
def orden_borrar(request, id):
    try:
        orden = Orden.objects.get(id = id)
        orden.delete()
        return redirect(reverse('ordenes:ordenes_lista') + '?DELETED')
    except:
        return redirect(reverse('ordenes:ordenes_lista') + '?FAIL')
    
def ordenes(request):
    if request.user.is_authenticated:
        ordenes = Orden.objects.filter(user=request.user.id)             
        return render(request, 'client/ordenes.html', {'ordenes' : ordenes})
    else:
        return redirect('home')
    
def orden_detalle(request, pk):
    if request.user.is_authenticated:
        orden = Orden.objects.get(id=pk)
        items = OrdenItem.objects.filter(orden=pk)
        return render(request, 'client/orden_detalle.html', {'orden' : orden, 'items' : items})
    else:
        return redirect('home')