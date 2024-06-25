from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Cupon
from carro.carro import Carro
from ordenes.models import Orden
from .forms import CuponForm

@require_POST
def aplicar_cupon(request):
    now = timezone.now()  
    form = CuponForm(request.POST)
    if form.is_valid():
        codigo = form.cleaned_data['codigo']
        try:
            cupon = Cupon.objects.get(codigo__iexact=codigo, valido_hasta__gte=now, activo=True)
            request.session['cupon_id'] = cupon.id
        except:
            request.session['cupon_id'] = None
    return redirect('ordenes:orden_nuevo')
