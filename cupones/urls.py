from django.urls import path
from .views import *

app_name='cupones'

urlpatterns = [
    path('aplicar/', aplicar_cupon, name='aplicar')
]
