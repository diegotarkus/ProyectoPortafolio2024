from django.urls import path
from .views import *

app_name='ordenes'

urlpatterns = [
    path('checkout/', orden_nuevo, name="orden_nuevo"),
    path('ordenes/', ordenes, name='ordenes'),
    path('orden/<int:pk>/', orden_detalle, name="orden_detalle"),
    path('admin/ordenlist/', ordenes_lista, name="ordenes_lista"),
    path('admin/estado/<int:id>', orden_estado, name="orden_estado"),  
    path('admin/editar/<int:id>', orden_editar, name='orden_editar'),
    path('admin/borrar/<int:id>', orden_borrar, name='orden_borrar'),
    
    path('api/v1/transbank/transaction/create/', webpay_create, name='webpay-create'),
    path('exito/', webpay_retorno, name='webpay-retorno')
]