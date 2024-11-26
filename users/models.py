from django.db import models
from django.contrib.auth.models import User
from administracion.models import Efectivo, Comisaria
from datetime import datetime

# Create your models here.

class Profile(models.Model):

    ADMINISTRADOR = 'Administrador'
    ENCARGADO = 'Encargado'

    TIPO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ENCARGADO, 'Encargado'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    tipo_usuario = models.CharField(max_length=25, choices=TIPO_CHOICES, default=ENCARGADO)
    administrador_de = models.OneToOneField(Comisaria, on_delete=models.DO_NOTHING, blank=True, null=True)

    esta_autorizado = models.BooleanField(default=False)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)

    def __str__(self):
        return f'Perfil de {self.user.username}.'
