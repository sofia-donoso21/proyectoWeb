from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.


class Mascotas(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    tipoMascota = models.CharField(max_length=10)
    adoptado = models.BooleanField()


class Vacunas(models.Model):
    idMascota = models.CharField(max_length=10)
    nombreVac = models.CharField(max_length=50)
    fechaVac = models.DateField()
    enfermedad = models.CharField(max_length=50)
    cantidadVac = models.CharField(max_length=2)
