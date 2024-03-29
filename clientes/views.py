from django.shortcuts import redirect, render
from ventas.models import Clientes, Egreso, Productos, ProductosEgreso
from clientes.forms import AddClienteForm, AddProductoForm, EditarClienteForm, EditarProductoForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import json
import os


# Create your views here.

def ventas_view(request):
    ventas = Egreso.objects.all()
    num_ventas = len(ventas)
    context = {
        'ventas': ventas,
        'num_ventas':num_ventas
    }
    return render(request, 'ventas.html', context)

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

class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Productos.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            elif action == 'save':
                total_pagado = float(request.POST['efectivo']) 
                + float(request.POST['tarjeta']) 
                + float(request.POST['transferencia']) 
                + float(request.POST['vales']) 
                + float(request.POST['otro'])
                fecha = request.POST['fecha']
                id_cliente = int(request.POST['id_cliente'])
                cliente_obj = Clientes.objects.get(pk=int(id_cliente))
                datos = json.loads(request.POST['verts'])
                total_venta = float(datos['total'])
                ticket_num = int(request.POST['ticket'])
                if ticket_num == 1:
                    ticket = True
                else:
                    ticket = False
                desglosar_IVA_num = int(request.POST['desglosar'])
                if desglosar_IVA_num == 0:
                    desglosar_IVA = False
                elif desglosar_IVA_num == 1:
                    desglosar_IVA = True
                comentarios = request.POST['comentarios']
                nueva_venta = Egreso(fecha_pedido=fecha, 
                                     cliente=cliente_obj, 
                                     total=total_venta, 
                                     pagado = total_pagado,
                                     desglosar_IVA=desglosar_IVA,
                                     comentarios=comentarios,
                                     ticket=ticket,
                                     desglosar=desglosar_IVA)
                nueva_venta.save()
                for i in datos['productos']:
                    producto_obj = Productos.objects.get(pk=int(i['id']))
                    nuevo_producto = ProductosEgreso(egreso=nueva_venta, 
                                                     producto=producto_obj, 
                                                     cantidad=int(i['cantidad']), 
                                                     subtotal=float(i['subtotal']))
                    nuevo_producto.save()
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_lista'] = Productos.objects.all()
        context['clientes_lista'] = Clientes.objects.all()
        return context


def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Mi empresa S.A. De C.V"
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response

def delete_venta_view(request):
    if request.method == 'POST':
        cliente = Egreso.objects.get(pk=request.POST.get('id_producto_eliminar'))
        cliente.delete()
        messages.success (request, 'Venta eliminada correctamente')
    return redirect ('Venta')