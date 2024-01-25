from django.db import models

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
