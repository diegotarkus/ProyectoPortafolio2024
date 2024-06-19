from .carro import Carro
from gestionPedidos.models import Categoria

def carro(request):
    return {'carro': Carro(request)}

def extras(request):
	lista_categorias = Categoria.objects.all().order_by('nombre')
	return {'lista_categorias':lista_categorias}

def importe_total_carro(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session['carro'].items():
                total = total + int(value['precio'])
    return {'importe_total_carro' : total}
