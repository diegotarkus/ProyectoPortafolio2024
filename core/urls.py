from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('crear_user/', crear_user, name='crear_user')
    #path('busqueda_productos/', busqueda_productos),
    #path('buscar/', buscar),
    #path('contacto/', contacto),
    
]