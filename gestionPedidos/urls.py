from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', lista_productos, name='productos'),
    path('producto_nuevo/', producto_nuevo, name='producto_nuevo'),
    path('productos/editar/<str:id_producto>', producto_editar, name='producto_editar'),
    path('productos/<str:id_producto>/borrar', producto_borrar, name='producto_borrar')
]

