from django.shortcuts import redirect, render
from ventas.models import Clientes, Productos
from clientes.forms import AddClienteForm, AddProductoForm, EditarClienteForm, EditarProductoForm
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

def productos_view(request):
    productos = Productos.objects.all()
    form_add = AddProductoForm()
    form_editar = EditarProductoForm()
    context = {
        'productos': productos,
        'form_add': form_add,
        'form_editar': form_editar,
    }
    return render(request, 'productos.html', context)

def add_producto_view(request):
    if request.method == 'POST':
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect('productos')
        else:
            messages.error(request, 'Error al agregar producto')
    else:
        form = AddProductoForm()

def edit_producto_view(request):
    if request.method == 'POST':
        try:
            producto = Productos.objects.get(pk=request.POST.get('id_personal_editar'))
        except Productos.DoesNotExist:
            messages.error(request, 'Producto no encontrado')
            return redirect('productos')

        form = EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado correctamente')
        else:
            messages.error(request, 'Hubo un error al editar el producto')

    return redirect('productos')


def delete_producto_view(request):
    if request.method == 'POST':
        producto = Productos.objects.get(pk=request.POST.get('id_personal_eliminar'))
        producto.delete()
        messages.success (request, 'Producto eliminado correctamente')
    return redirect ('productos')