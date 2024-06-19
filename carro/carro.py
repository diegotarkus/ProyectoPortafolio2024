from django.conf import settings
from decimal import Decimal
from gestionPedidos.models import Producto

class Carro(object):
    def __init__(self, request):
        self.session = request.session
       #self.coupon_id = self.session.get('coupon_id')
        carro = self.session.get(settings.CARRO_SESSION_ID)
        if not carro:
            carro = self.session[settings.CARRO_SESSION_ID] = {}
        self.carro = carro
        
    def anadir(self, producto, cantidad=1):
        if(str(producto.id_producto) not in self.carro.keys()):
            self.carro[producto.id_producto]={
                'id_producto' : producto.id_producto,
                'nombre' : producto.nombre,
                'precio' : producto.precio,
                'cantidad' : 1,
                'imagen' : producto.imagen.url                
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id_producto):
                    value['cantidad']= value['cantidad']+ 1
                    value['precio']= value['precio']+ producto.precio
                    break
        self.guardar()
        
    def guardar (self):
        self.session["carro"]=self.carro
        self.session.modified=True
        
    def eliminar (self, producto):
        producto.id_producto=str(producto.id_producto)
        if producto.id_producto in self.carro:
            del self.carro[producto.id_producto]
            self.guardar()
    
    def remover (self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id_producto):
                value['cantidad'] = value['cantidad']-1
                value['precio'] = value['precio']-producto.precio
                if value['cantidad']<1:
                    self.eliminar(producto)
                    break
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
            item['precio'] = item['precio']
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item
            
    def __len___(self):
        return sum(item['cantidad'] for item in self.carro.values())
    
    def precio_total(self):
        return sum(Decimal(item['precio']) * item['cantidad'] for item in self.carro.values())
    
         