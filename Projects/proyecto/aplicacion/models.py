from django.db import models

# Create your models here.

class Autor(models.Model):
    #autorId =models.AutoField()
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    #autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    isbn = models.CharField(primary_key = True)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField( max_length=100)

class Reseña(models.Model):

    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)
    comentario = models.CharField( max_length = 300)

class Calificacion(models.Model):

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    calificacion = models.IntegerField() 
