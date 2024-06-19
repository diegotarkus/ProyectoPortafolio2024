from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from guest_user.decorators import allow_guest_user
from .forms import OrdenForm, OrdenFormAdmin
from .models import Orden, OrdenItem
from gestionPedidos.models import Producto
from carro.carro import Carro

User = get_user_model()

@allow_guest_user
def orden_nuevo(request):
    carro = Carro(request)
    usuario = User.objects.get(username=request.user.username)
    print(usuario)
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
            user = usuario
            orden = Orden.objects.create(
                nombre = nombre,
                apellido = apellido,
                direccion = direccion,
                comuna = comuna,
                ciudad = ciudad,
                telefono = telefono,
                comentario = comentario,
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
    return render(request, 'checkout.html', {'carro' : carro, 'form' : form})

@staff_member_required
def ordenes_lista(request):
    context = {'ordenes' : Orden.objects.all()}
    return render(request,'admin/ordenlist.html',context)

@staff_member_required
def orden_editar(request, id):
    try:
        orden = Orden.objects.get(id = id)
        form = OrdenFormAdmin(instance = orden)

        if request.method == 'POST':
            form = OrdenFormAdmin(request.POST, instance = orden)
            if form.is_valid():
                form.save()
                return redirect(reverse('ordenes') + '?UPDATED')
            else:
                return redirect(reverse('orden_editar') + id_producto) 

        context = {'form' : form}
        return render(request,'orden_editar.html', context)
    except:
        return redirect(reverse('ordenes') + '?NO_EXISTS')
    
@staff_member_required   
def orden_borrar(request, id):
    try:
        orden = Orden.objects.get(id = id)
        orden.delete()
        return redirect(reverse('ordenes') + '?DELETED')
    except:
        return redirect(reverse('ordenes') + '?FAIL')

