from django import forms
from ventas.models import Clientes

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