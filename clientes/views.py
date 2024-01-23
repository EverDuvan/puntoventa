from django.shortcuts import redirect, render
from ventas.models import Clientes
from clientes.forms import AddClienteForm, EditarClienteForm
from django.contrib import messages

# Create your views here.


def clientes_view(request):
    clientes = Clientes.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    form = AddClienteForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success (request, 'Cliente agregado correctamente')
    else:
        messages.error(request, 'Error al agregar cliente')
    return redirect ('clientes')

def edit_cliente_view(request):
    if request.method == 'POST':
        cliente = Clientes.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(request.POST,request.FILES, instance=cliente)
        messages.success (request, 'Cliente editado correctamente')
        if form.is_valid():
            form.save()
    return redirect ('clientes')

def delete_cliente_view(request):
    if request.method == 'POST':
        cliente = Clientes.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
        messages.success (request, 'Cliente eliminado correctamente')
    return redirect ('clientes')