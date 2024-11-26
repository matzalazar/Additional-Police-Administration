from django.db import models
from django.contrib.auth.models import User
from administracion.models import Efectivo, Comisaria
from users.models import Profile
from datetime import datetime

# Create your models here.

class Cores(models.Model):

    OPERATIVAS = 'OP'
    CHOFERES = 'OP CHOF'
    NO_OPERATIVAS = 'NO OP'

    TIPO_CHOICES = [
        (OPERATIVAS, 'OPERATIVAS'),
        (NO_OPERATIVAS, 'NO OPERATIVAS'),
        (CHOFERES, 'OPERATIVAS CHOFERES'),
    ]

    ingreso = models.DateTimeField(null=True)
    egreso = models.DateTimeField(null=True)
    efectivo = models.ForeignKey(Efectivo, on_delete=models.DO_NOTHING)
    tipo = models.CharField(max_length=13, choices=TIPO_CHOICES, default=OPERATIVAS)
    dependencia = models.ForeignKey(Comisaria, default=None, on_delete=models.DO_NOTHING)

    @property
    def get_diff(self):
        return int((self.egreso - self.ingreso).total_seconds()/60/60)

    def __str__(self):
        return f'{self.ingreso} a {self.egreso}: {self.efectivo}. Cantidad de horas: {self.get_diff}.'
