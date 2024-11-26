from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):

    remitente = models.ForeignKey(User, related_name="remitente", on_delete=models.DO_NOTHING)
    destinatario = models.ForeignKey(User, related_name="destinatario", on_delete=models.DO_NOTHING)
    mensaje = models.CharField(max_length=1024)
    creado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.remitente} a {self.destinatario}.'
