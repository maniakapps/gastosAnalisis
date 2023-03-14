from django.shortcuts import render, redirect

from manejogastos.forms import NuevaCuentaForm, NuevoGastoForm
from manejogastos.models import CuentaBancaria, Gasto


# Create your views here.
def agregar_cuenta(request):
    if request.method == 'POST':
        form = NuevaCuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cuentas')
    else:
        form = NuevaCuentaForm()
    return render(request, 'agregar_cuenta.html', {'form': form})


def lista_cuentas(request):
    cuentas = CuentaBancaria.objects.all()
    return render(request, 'lista_cuentas.html', {'cuentas': cuentas})


def agregar_gasto(request):
    if request.method == 'POST':
        form = NuevoGastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        form = NuevoGastoForm()
    return render(request, 'agregar_gasto.html', {'form': form})


def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'lista_gastos.html', {'gastos': gastos})
