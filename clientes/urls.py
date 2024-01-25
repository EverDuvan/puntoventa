from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.clientes_view, name='clientes'),
    path('add_clientes', views.add_cliente_view, name='AddCliente'),
    path('edit_clientes', views.edit_cliente_view, name='EditCliente'),
    path('delete_clientes', views.delete_cliente_view, name='DeleteCliente'),
    path('productos/', views.productos_view, name='productos'),
    path('add_productos', views.add_producto_view, name='AddProducto'),
    path('edit_productos', views.edit_producto_view, name='EditProducto'),
    path('delete_productos', views.delete_producto_view, name='DeleteProducto'),

]