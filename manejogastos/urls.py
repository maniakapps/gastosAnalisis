from django.urls import path
from . import views

urlpatterns = [
    path('agregar-gasto/', views.agregar_gasto, name='agregar_gasto'),
    path('lista-gastos/', views.lista_gastos, name='lista_gastos'),
    path('agregar-cuenta/', views.agregar_cuenta, name='agregar_cuenta'),
    path('lista-cuentas/', views.lista_cuentas, name='lista_cuentas'),
]
