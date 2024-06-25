from django.contrib import admin
from core.models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display=("creado", "nombre", "correo")
    list_filter=("creado", "nombre", "correo")

admin.site.register(Contacto)


