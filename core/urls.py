from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registrar/', registrar, name='registrar'),
    path('categoria/<str:id>/', categoria, name='categoria'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', exit, name='logout'),
    path('productos/<str:id_producto>', detalle_producto, name='detalle_producto')
    
    #path('busqueda_productos/', busqueda_productos),
    #path('buscar/', buscar),
    #path('contacto/', contacto),
    
]