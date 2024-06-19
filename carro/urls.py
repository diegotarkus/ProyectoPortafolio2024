from django.urls import path
from .import views

app_name = "carro"

urlpatterns = [
    path('detalle_carro/', views.detalle_carro, name='detalle_carro'),
    path('anadir/<id_producto>/', views.carro_mas, name='carro_mas'),
    path('restar/<id_producto>/', views.carro_menos, name='carro_menos'),
    path('limpiar/', views.carro_limpiar, name='carro_limpiar')
]
