from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from .models import *
from gestionPedidos.models import Producto
from .forms import *
import bcrypt

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    context = {'productos': Producto.objects.all()}
    return render(request, "home.html", context)

def crear_user(request):
    if request.method == 'POST':
        errors = Cliente.objects.validador(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
                request.session['registro_nombre'] = request.POST['nombre']
                request.session['registro_apellido'] = request.POST['apellido']
                request.session['registro_email'] = request.POST['correo']
                request.session['level_mensaje'] = 'alert-danger'

        else:
            request.session['registro_nombre'] = ""
            request.session['registro_apellido'] = ""
            request.session['registro_email'] = ""
            
            rut = request.POST['rut']
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['correo']
            telefono = request.POST['telefono']
            direccion = request.POST['direccion']
            password = request.POST['password']
            password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            
            obj = Cliente.objects.create(
                rut=rut,
                nombre=nombre, 
                apellido=apellido,
                correo=correo,
                telefono=telefono,
                direccion=direccion,
                password_decode=password,
                password=password_hash
            )
            obj.save()
            messages.success(request, "Usuario registrado.")
            request.session['level_mensaje'] = 'alert-success'
            
            return redirect(reverse('home')+ '?OK')
        
    return render(request,'crear_user.html')
    

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" %request.GET["prd"]
        prdcto=request.GET["prd"]

        if len(prdcto)>20:
            mensaje="Texto de búsqueda demasiado largo"
        else:

            producto=Producto.objects.filter(nombre__icontains=prdcto)
            return render(request, "resultados_busqueda.html", {"producto":producto, "query":producto})
    
    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")
    return render(request, "contacto.html")
