from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

class Empleado(models.Model):
    #
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    antiguedad = models.IntegerField(default = 0)