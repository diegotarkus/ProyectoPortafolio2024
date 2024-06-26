from django.urls import path
from .views import *

app_name='ordenes'

urlpatterns = [
    path('checkout/', orden_nuevo, name="orden_nuevo"),
    path('ordenes/', ordenes, name='ordenes'),
    path('ordenes/<int:pk>/', orden_detalle, name="orden_detalle"),
    path('admin/ordenlist/', ordenes_lista, name="ordenes_lista"),
    path('ordenes/editar/<int:id>', orden_editar, name='orden_editar'),
    path('ordenes/borrar/<str:id>', orden_borrar, name='orden_borrar')
]
