from django.contrib import admin
from .models import Cupon

class CuponAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'valido_hasta', 'descuento', 'activo']
    list_filter = ['activo', 'valido_hasta']
    search_fields = ['codigo']

admin.site.register(Cupon, CuponAdmin)
