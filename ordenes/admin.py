from django.contrib import admin
from .models import *

class OrdenItemInline(admin.TabularInline):
	model = OrdenItem
	raw_id_fields = ['producto']

class OrdenesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'creada', 'estado')
    list_filter = ('id', 'user', 'creada', 'estado')
    inlines = [OrdenItemInline]

admin.site.register(Orden, OrdenesAdmin)
admin.site.register(OrdenItem)