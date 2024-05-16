from django.shortcuts import render

# Create your views here.

def root(request):
    return redirect('/home')

def home(request):
    return render(request, "home.html")

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
