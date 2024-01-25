from django import forms
from ventas.models import Clientes, Productos

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono', 'direccion', 'email')
        labels = {
            'codigo': 'Codigo cliente:',
            'nombre': 'Nombre:',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono', 'direccion', 'email')
        labels = {
            'codigo': 'Codigo cliente:',
            'nombre': 'Nombre:',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'direccion': forms.TextInput(attrs={'id': 'direccion_editar'}),
            'email': forms.TextInput(attrs={'id': 'email_editar'}),
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('codigo', 'descripcion', 'costo', 'precio', 'cantidad', 'imagen')
        labels = {
            'codigo': 'Codigo producto:',
            'descripcion': 'Descripcion:',
            'costo': 'Costo:',
            'precio': 'Precio:',
            'cantidad': 'Cantidad:',
            'imagen': 'Imagen:',
        }

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('codigo', 'descripcion', 'costo', 'precio', 'cantidad', 'imagen')
        labels = {
            'codigo': 'Codigo producto:',
            'descripcion': 'Descripcion:',
            'costo': 'Costo:',
            'precio': 'Precio:',
            'cantidad': 'Cantidad:',
            'imagen': 'Imagen:',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id': 'costo_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_editar'}),
            #imagen': forms.TextInput(attrs={'id': 'imagen_editar'}),
        }