from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Clientes(models.Model):
    codigo = models.CharField(max_length=10, null = True, blank = False)
    nombre = models.CharField(max_length=50, null = True, blank = False)
    telefono = models.CharField(max_length=20, null = True, blank = False)
    direccion = models.CharField(max_length=70, null = True, blank = False)
    email = models.EmailField()
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    codigo = models.CharField(max_length=10, null = True, blank = True)
    descripcion = models.CharField(max_length=50, null = True, blank = True)
    imagen = models.ImageField(upload_to="productos", null = True, blank = True)
    costo = models.IntegerField(default=0, null = True, blank = True)
    precio = models.IntegerField(default=0, null = True, blank = True)
    cantidad = models.IntegerField(null = True, blank = True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.descripcion
    
class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item
