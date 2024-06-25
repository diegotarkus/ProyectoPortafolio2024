from django.contrib import admin
from .models import *

class OrdenItemInline(admin.StackedInline):
    model = OrdenItem
    extra = 0
    raw_id_fields = ['producto']

class OrdenesAdmin(admin.ModelAdmin):
    readonly_fields = ["creada"]
    list_display = ('id', 'user', 'total_oc', 'estado')
    list_filter = ('id', 'user', 'creada', 'total_oc', 'estado')
    inlines = [OrdenItemInline]

admin.site.register(Orden, OrdenesAdmin)
admin.site.register(OrdenItem)