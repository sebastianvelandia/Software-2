from django.db import models

# Create your models here.

class Autor(models.Model):
    autorId = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    isbn = models.CharField(primary_key = True, max_length=13)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField( max_length=100)

class Reseña(models.Model):
    reseñaId = models.AutoField(primary_key = True)
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    comentario = models.CharField( max_length = 300)

class Calificacion(models.Model):
    calificacionId = models.AutoField(primary_key = True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    calificacion = models.IntegerField() 

