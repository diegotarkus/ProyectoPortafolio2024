from django.urls import path
from .views import *

urlpatterns = [
    path('producto_nuevo/', producto_nuevo, name='producto_nuevo'),
    path('productos/', lista_productos, name='productos'),
]

