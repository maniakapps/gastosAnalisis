from django import forms
from django.forms import SelectDateWidget
from django.utils.translation import gettext_lazy as _

from .models import CuentaBancaria, Gasto, CategoriaGasto


class NuevaCuentaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ['nombre_banco', 'numero_cuenta']
        labels = {
            'nombre_banco': _('Nombre del banco'),
            'numero_cuenta': _('Número de cuenta'),
        }
        help_texts = {
            'nombre_banco': _('Ingrese el nombre de su banco.'),
            'numero_cuenta': _('Ingrese el número de cuenta.'),
        }

    def clean_numero_cuenta(self):
        nombre_banco = self.cleaned_data['nombre_banco']
        numero_cuenta = self.cleaned_data['numero_cuenta']
        cuenta_existente = CuentaBancaria.objects.filter(nombre_banco=nombre_banco, numero_cuenta=numero_cuenta).first()
        if cuenta_existente:
            raise forms.ValidationError(
                _("Ya existe una cuenta con el número de cuenta {numero_cuenta} en el banco {nombre_banco}.")
                .format(numero_cuenta=numero_cuenta, nombre_banco=nombre_banco))
        return numero_cuenta


class NuevoGastoForm(forms.ModelForm):
    fecha = forms.DateField(widget=SelectDateWidget(), label=_('Fecha'), help_text=_('Seleccione la fecha del gasto.'))
    categoria = forms.ModelChoiceField(queryset=CategoriaGasto.objects.all(), label=_('Categoría'),
                                       help_text=_('Seleccione una categoría para el gasto.'))

    class Meta:
        model = Gasto
        fields = ['fecha', 'monto', 'categoria', 'descripcion', 'cuenta_bancaria']
        labels = {
            'monto': _('Monto'),
            'categoria': _('Categoría'),
            'descripcion': _('Descripción'),
            'cuenta_bancaria': _('Cuenta bancaria'),
        }
        help_texts = {
            'monto': _('Ingrese el monto del gasto.'),
            'categoria': _('Seleccione una categoría para el gasto.'),
            'descripcion': _('Ingrese una descripción breve del gasto.'),
            'cuenta_bancaria': _('Seleccione la cuenta bancaria asociada al gasto.'),
        }

    def clean_monto(self):
        monto = self.cleaned_data['monto']
        if monto <= 0:
            raise forms.ValidationError(_("El monto del gasto debe ser mayor a cero."))
        return monto
