from django.db import models


# Create your models here.
class CuentaBancaria(models.Model):
    nombre_banco = models.CharField(max_length=255)
    numero_cuenta = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre_banco} - {self.numero_cuenta}"


class Gasto(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2, default='0.0')
    categoria = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    cuenta_bancaria = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} - {self.monto} - {self.categoria}"


class CategoriaGasto(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'
