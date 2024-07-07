from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST
from guest_user.mixins import RegularUserRequiredMixin
from .models import Cupon
from carro.carro import Carro
from ordenes.models import Orden
from .forms import CuponForm

@require_POST
def aplicar_cupon(request):
    now = timezone.now()  
    form = CuponForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            try:
                cupon = Cupon.objects.get(codigo__iexact=codigo, valido_hasta__gte=now, activo=True)
                request.session['cupon_id'] = cupon.id
            except:
                request.session['cupon_id'] = None
                return redirect(reverse('ordenes:orden_nuevo') + '?NO_EXISTS')
        return redirect(reverse('ordenes:orden_nuevo') + '?OK')
