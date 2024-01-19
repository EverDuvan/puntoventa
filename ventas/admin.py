from django.contrib import admin
from ventas.models import Productos, Clientes

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields = ['nombre']
    readonly_fields = ('Updated', 'Created')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Clientes, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'precio', 'cantidad')
    search_fields = ['descripcion']
    readonly_fields = ('Updated', 'Created')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Productos, ProductoAdmin)