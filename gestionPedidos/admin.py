from django.contrib import admin
from gestionPedidos.models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("id_producto", "nombre", "precio")
    list_filter=("id_producto",)
    

admin.site.register(Producto, ProductoAdmin)


