from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comisaria(models.Model):

    dependencia = models.CharField(max_length=100)
    es_cabecera = models.BooleanField(default=False)

    def __str__(self):
        return self.dependencia

class Efectivo(models.Model):

    OFL = "OFL"
    SGTO = "SGTO"
    SUBTTE = "SUBTTE"
    TTE = "TTE"
    TTE1ERO = "TTE1ERO"
    CAP = "CAP"
    MAYOR = "MAYOR"
    OSA = "OSA"
    OA = "OA"
    OSI = "OSI"
    OI = "OI"
    PPAL = "PPAL"
    SUBCRIO = "SUBCRIO"
    CRIO = "CRIO"

    JERARQUIA_CHOICES = [
        (OFL, 'OFL'),
        (SGTO, 'SGTO'),
        (SUBTTE, 'SUBTTE'),
        (TTE, 'TTE'),
        (TTE1ERO, 'TTE1ERO'),
        (CAP, 'CAP'),
        (MAYOR, 'MAYOR'),
        (OSA, 'OSA'),
        (OA, 'OA'),
        (OSI, 'OSI'),
        (OI, 'OI'),
        (PPAL, 'PPAL'),
        (SUBCRIO, 'SUBCRIO'),
        (CRIO, 'CRIO'),
        ]

    ITEM_1 = "1"
    ITEM_2 = "2"
    ITEM_3 = "3"
    ITEM_4 = "4"
    ITEM_5 = "5"
    ITEM_6 = "6"

    ITEM_CHOICES = [
        (ITEM_1, "1"),
        (ITEM_2, "2"),
        (ITEM_3, "3"),
        (ITEM_4, "4"),
        (ITEM_5, "5"),
        (ITEM_6, "6"),
    ]

    efectivo_nombre = models.CharField(max_length=200)
    efectivo_legajo = models.IntegerField()
    efectivo_dni = models.IntegerField()
    efectivo_jerarquia = models.CharField(max_length=20, choices=JERARQUIA_CHOICES, default=OFL)
    efectivo_item = models.CharField(max_length=8, choices=ITEM_CHOICES, default= ITEM_1)

    def __str__(self):
        return self.efectivo_nombre
