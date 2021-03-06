from rest_framework import serializers
from HistoriaApp.models import Autor, Libro, Calificacion, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields =('autorId','nombre',)

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model= Libro
        fields=('isbn','autores','titulo')

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ('libro', 'comentario')

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ('libro', 'calificacion')
