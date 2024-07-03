from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registrar/', registrar, name='registrar'),
    path('categoria/<str:foo>/', categoria, name='categoria'),
    path('ver-orden/', busca_ordenes, name='busca-ordenes'),
    path('contacto/', contacto, name='contacto'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', exit, name='logout'),
    path('productos/<str:id_producto>', detalle_producto, name='detalle_producto')
]