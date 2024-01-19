from django.shortcuts import render
from ventas.models import Clientes

# Create your views here.


def clientes_view(request):
    clientes = Clientes.objects.all()
    context = {
        'clientes': clientes,
    }
    return render(request, 'clientes.html', context)