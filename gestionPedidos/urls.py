from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', lista_productos, name='productos'),
    path('categoria_nuevo/', categoria_nuevo, name='categoria_nuevo'),
    path('producto_nuevo/', producto_nuevo, name='producto_nuevo'),
    path('productos/editar/<str:id_producto>', producto_editar, name='producto_editar'),
    path('productos/borrar/<str:id_producto>', producto_borrar, name='producto_borrar')
]

