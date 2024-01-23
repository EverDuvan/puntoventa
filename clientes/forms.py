from django import forms
from ventas.models import Clientes

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente:',
            'nombre': 'Nombre:',
            'telefono': 'Telefono'
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente:',
            'nombre': 'Nombre:',
            'telefono': 'Telefono'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }