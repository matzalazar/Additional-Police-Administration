from django.db import models
from django.contrib.auth.models import User
from administracion.models import Comisaria, Efectivo
from datetime import datetime
from .choices import CITY_CHOICES

# Create your models here.

class Adicional(models.Model):

    primera = '1era'
    segunda = '2da'
    tercera = '3era'
    cuarta = '4ta'
    quinta = '5ta'

    CAT_CHOICES = [
        (primera, '1era'),
        (segunda, '2da'),
        (tercera, '3era'),
        (cuarta, '4ta'),
        (quinta, '5ta'),
    ]

    numero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    categoria = models.CharField(max_length=4, choices=CAT_CHOICES, default=None)
    localidad = models.CharField(max_length=50, choices=CITY_CHOICES, default=None)
    comisaria = models.ForeignKey(Comisaria, default=None, on_delete=models.DO_NOTHING)
    entidad_contratante = models.CharField(max_length=100)
    cuenta_corriente = models.CharField(max_length=100)
    encargado = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)

    puede_rendir = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.numero}: {self.nombre}.'

class Turno(models.Model):

    polad = models.ForeignKey(Adicional, default=None, on_delete=models.DO_NOTHING)

    ingreso = models.DateTimeField(null=True)
    egreso = models.DateTimeField(null=True)
    efectivo = models.ForeignKey(Efectivo, on_delete=models.DO_NOTHING)

    @property
    def get_diff(self):
        return int((self.egreso - self.ingreso).total_seconds()/60/60)

    def __str__(self):
        return f'{self.ingreso.day}/{self.ingreso.month} de {self.ingreso.hour} hasta {self.egreso.hour}: {self.efectivo}.'
