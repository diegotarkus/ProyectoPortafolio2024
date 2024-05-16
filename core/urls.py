from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    #path('busqueda_productos/', busqueda_productos),
    #path('buscar/', buscar),
    #path('contacto/', contacto),
    
]