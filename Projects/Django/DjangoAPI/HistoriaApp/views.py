from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from HistoriaApp.models import Autor, Libro, Calificacion, Reseña
from HistoriaApp.serializers import AutorSerializer, LibroSerializer, ReseñaSerializer, CalificacionSerializer
# Create your views here.

@csrf_exempt
def autorApi(request, id=0):
    if(request.method == 'GET'):
        autores = Autor.objects.all()
        autores_serializer = AutorSerializer(autores, many = True) 
        print("GET")
        return JsonResponse(autores_serializer.data, safe = False)
    
    elif(request.method == 'POST'):
        autor_data = JSONParser().parse(request)
        autor_serializer = AutorSerializer(data = autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('Agregado correctamente', safe =False)
        return JsonResponse('Fallo al agregar', safe = False)

    elif(request.method == 'PUT'):
        autor_data = JSONParser().parse(request)
        autor = Autor.objects.get(AutorId=autor_data['id'])
        autor_serializer = AutorSerializer(autor, data=autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('actualizado correctamente', safe =False)
        return JsonResponse('Fallo al actualizar', safe = False)

    elif request.method == 'DELETE':
        autor = Autor.objects.get(AutorId=id)
        autor.delete()
        return JsonResponse('Borrado correctamente', safe = False)