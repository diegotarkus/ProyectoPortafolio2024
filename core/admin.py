from django.contrib import admin
from core.models import Cliente, Pedido, Descuento, Estado

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("rut", "nombre", "apellido", "correo")
    search_fields=("correo", "nombre")

class PedidoAdmin(admin.ModelAdmin):
    list_display=("id_pedido", "nombre")
    list_filter=("id_pedido",)
    
admin.site.register(Cliente, ClienteAdmin)    
admin.site.register(Pedido, PedidoAdmin)    
admin.site.register(Descuento)
admin.site.register(Estado)
