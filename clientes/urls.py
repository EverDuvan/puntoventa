from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes_view, name='clientes'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('add_clientes', views.add_cliente_view, name='AddCliente'),
    path('edit_clientes', views.edit_cliente_view, name='EditCliente'),
    path('delete_clientes', views.delete_cliente_view, name='DeleteCliente'),

]