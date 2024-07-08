from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import transaction
from guest_user.decorators import allow_guest_user
from .forms import OrdenForm, OrdenFormAdmin
from cupones.models import Cupon
from cupones.forms import CuponForm
from .models import Orden, OrdenItem, Transaccion
from gestionPedidos.models import Producto
from carro.carro import Carro
import requests
import random
import json
import datetime

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
    else:
        cupon = None
        descuento = 0
        
    if request.method == 'POST':
        try:
            transaction.set_autocommit(False)
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
                
                transaction.commit()                
                return render(request, 'crear.html', {'orden' : orden})
        except:
            transaction.rollback()
            return redirect("/")
        finally:
            transaction.set_autocommit(True)
    else:
        form = OrdenForm()
        cuponform = CuponForm()
        context = {'carro' : carro, 'form' : form, 'cuponform' : CuponForm}
        return render(request, 'checkout.html', context)
    
def header_request_transbank():
    headers = {
        "Authorization": "Token",
        "Tbk-Api-Key-Id": "597055555532",
        "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        'Referrer-Policy': 'origin-when-cross-origin',
    }
    return headers

def webpay_create(request):
    carro = Carro(request)
    usuario = User.objects.get(username=request.user.username)
    subtotal = carro.carro_total()
    if carro.cupon:
        cupon = carro.cupon
        descuento = carro.descuento()
        desc = Cupon.desc(cupon)
        print("desc:", desc)
    else:
        cupon = None
        descuento = 0
    # Calcula el valor total sumando los subtotales de los productos en el carrito
    total = int(carro.total())

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
            
            #return render(request, 'crear.html', {'orden' : orden})
        
        data = {
            "buy_order": str(random.randrange(1000000, 99999999)),
            "session_id": str(random.randrange(1000000, 99999999)),
            "amount": total,
            "return_url": "http://127.0.0.1:8000/ordenes/exito",
        }
        url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions"
        headers = header_request_transbank()
        respuesta = requests.post(url, json=data, headers=headers)

        if respuesta.status_code == 200:
            response = respuesta.json()
            newurl = response.get('url')
            tokenrs = response.get('token')
            print("json: ")
            print(response)
            print("url: ")
            print(newurl)
            print("token: ")
            print(tokenrs)
            return render(request, 'crear.html', {
                'url': newurl, 
                'token': tokenrs, 
                'total': total, 
                'respuesta' : respuesta})
        else:
            return HttpResponse('Error al enviar la solicitud al servidor de Transbank')

    return HttpResponseBadRequest('Método no permitido')

def webpay_retorno(request):
    orden = Orden.objects.latest()
    token = request.GET.get('token_ws')
    data = {'token' : token}
    url = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/"+token
    headers = header_request_transbank()
    respuesta = requests.put(url, json=data, headers=headers)    
    if respuesta.status_code == 200:
        response = respuesta.json()
        vci = response.get('vci')
        status = response.get('status')
        print(status)
        buy_order = response.get('buy_order')
        session_id = response.get('session_id')
        card_detail = response.get('card_detail')
        card_number = json.dumps([card_detail][0]['card_number']).replace('"', '')
        accounting_date = response.get('accounting_date')
        transaction_date = response.get('transaction_date')
        fecha = datetime.datetime.fromisoformat(transaction_date)
        print(fecha)
        authorization_code = response.get('authorization_code')
        payment_type_code = response.get('payment_type_code')
        response_code = response.get('response_code')
        installments_number = response.get('installments_number')
        orden = orden
        if status == "AUTHORIZED":
            transaccion = Transaccion.objects.create(
                vci = vci,
                status = status,
                buy_order = buy_order,
                session_id= session_id,
                card_number = card_number,
                accounting_date = accounting_date,
                transaction_date = transaction_date,
                authorization_code = authorization_code,
                payment_type_code = payment_type_code,
                response_code = response_code,
                installments_number = installments_number,
                orden = orden
            )
            return render(request, 'exito.html', {'orden' : orden, 'fecha':fecha, 'respuesta' : respuesta, 'transaccion' : transaccion})
        else:
            return render(request, 'rechazado.html')
            

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

def exito(request):
    orden = Orden.objects.latest("id")
    return render(request, {'orden' : orden})