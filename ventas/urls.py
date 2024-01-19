from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_view, name='ventas'),
    #path('clientes/', views.clientes_view, name='clientes'),
]
