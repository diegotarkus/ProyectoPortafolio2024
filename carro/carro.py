from django.conf import settings
from decimal import Decimal
from cupones.models import Cupon
from gestionPedidos.models import Producto

class Carro(object):
    def __init__(self, request):
        self.session = request.session
        carro = self.session.get(settings.CARRO_SESSION_ID)
        if not carro:
            carro = self.session[settings.CARRO_SESSION_ID] = {}
        self.carro = carro
        self.cupon_id = self.session.get('cupon_id')
        
    def anadir(self, producto, cantidad=1, update=False):
        id_producto = str(producto.id_producto)
        if id_producto not in self.carro:
            self.carro[id_producto] = {'cantidad': 0, 'precio': str(producto.precio)}
        if update:
            self.carro[id_producto]['cantidad'] = cantidad
        else:
            self.carro[id_producto]['cantidad'] += cantidad
        self.guardar()
        
    def guardar (self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar (self, producto):
        producto.id_producto=str(producto.id_producto)
        if producto.id_producto in self.carro:
            del self.carro[producto.id_producto]
            self.guardar()
            
    def limpiar (self):
        self.session["carro"]={}
        self.session.modified=True
        
    def __iter__(self):
        producto_ids = self.carro.keys()
        productos = Producto.objects.filter(id_producto__in = producto_ids)
        for producto in productos:
            self.carro[str(producto.id_producto)]['producto'] = producto
            
        for item in self.carro.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item
            
    def __len___(self):
        return sum(item['cantidad'] for item in self.carro.values())
    
    def carro_total(self):
        carro_total = sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())
        return carro_total    
 
    @property
    def cupon(self):    
        if self.cupon_id:
            return Cupon.objects.get(id=self.cupon_id)      
        else:
            return None
        
    def descuento(self):
        if self.cupon:
            return (self.cupon.descuento / Decimal('100')) * self.carro_total()
        else:
            return 0
        
    def total(self):
        return self.carro_total() - self.descuento()
 
         
    