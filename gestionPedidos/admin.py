from django.contrib import admin
from gestionPedidos.models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ('id', 'nombre')

class ProductoAdmin(admin.ModelAdmin):
    list_display=("id_producto", "nombre", "precio")
    list_filter=("id_producto",)
    

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)


