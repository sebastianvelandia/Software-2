from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from HistoriaApp.models import Autor, Libro, Calificacion, Resena
from HistoriaApp.serializers import AutorSerializer, LibroSerializer, ResenaSerializer, CalificacionSerializer
# Create your views here.

@csrf_exempt
def autorApi(request, id=0):
    #Obtener cada autor
    if(request.method == 'GET'):
        if('name' in request.GET):
            autores = Autor.objects.filter(nombre__contains=request.GET['name'])
            autores_serializer = AutorSerializer(autores, many = True)
        else:
            autores = Autor.objects.all()  
            autores_serializer = AutorSerializer(autores, many = True)  
        return JsonResponse(autores_serializer.data, safe = False)
    #Agregar autor
    elif(request.method == 'POST'):
        autor_data = JSONParser().parse(request)
        autor_serializer = AutorSerializer(data = autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('Agregado correctamente', safe =False)
        return JsonResponse('Fallo al agregar', safe = False)
    #actualiza autor
    elif(request.method == 'PUT'):
        autor_data = JSONParser().parse(request)
        autor = Autor.objects.get(autorId=autor_data['autorId'])
        autor_serializer = AutorSerializer(autor, data=autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('actualizado correctamente', safe =False)
        return JsonResponse('Fallo al actualizar', safe = False)
    #elimina autor
    elif request.method == 'DELETE':
        autor = Autor.objects.get(autorId=id)
        autor.delete()
        return JsonResponse('Borrado correctamente', safe = False)

@csrf_exempt
def libroApi(request, id=0):
    if(request.method == 'GET'):
        if('isbn' in request.GET):
            libros = Libro.objects.filter(isbn=request.GET['isbn'])
        else:
            libros = Libro.objects.all()
        libros_serializer = LibroSerializer(libros, many = True)
        return JsonResponse(libros_serializer.data, safe = False)
    
    elif(request.method == 'POST'):
        libro_data = JSONParser().parse(request)
        libro_serializer = LibroSerializer(data = libro_data)
        print(libro_data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse('Agregado correctamente', safe =False)
        return JsonResponse('Fallo al agregar', safe = False)

    elif(request.method == 'PUT'):
        libro_data = JSONParser().parse(request)
        libro = Libro.objects.get(isbn=libro_data['isbn'])
        libro_serializer = AutorSerializer(libro, data=libro_data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse('Actualizado correctamente', safe =False)
        return JsonResponse('Fallo al actualizar', safe = False)

    elif request.method == 'DELETE':
        libro = Libro.objects.get(libroId=id)
        libro.delete()
        return JsonResponse('Borrado correctamente', safe = False)

@csrf_exempt
def resenaApi(request, id=0):
    if(request.method == 'GET'):
        resenas = Resena.objects.all()
        resenas_serializer = ResenaSerializer(resenas, many = True)
        return JsonResponse(resenas_serializer.data, safe = False)
    
    elif(request.method == 'POST'):
        resena_data = JSONParser().parse(request)
        resena_serializer = ResenaSerializer(data = resena_data)
        if resena_serializer.is_valid():
            resena_serializer.save()
            return JsonResponse('Agregado correctamente', safe =False)
        return JsonResponse('Fallo al agregar', safe = False)

    elif(request.method == 'PUT'):
        resena_data = JSONParser().parse(request)
        resena = Resena.objects.get(resenaId=resena_data['resenaId'])
        resena_serializer = AutorSerializer(resena, data=resena_data)
        if resena_serializer.is_valid():
            resena_serializer.save()
            return JsonResponse('Actualizado correctamente', safe =False)
        return JsonResponse('Fallo al actualizar', safe = False)

    elif request.method == 'DELETE':
        resena = Resena.objects.get(resenaId=id)
        resena.delete()
        return JsonResponse('Borrado correctamente', safe = False)


@csrf_exempt
def calificacionApi(request, id=0):
    if(request.method == 'GET'):
        calificaciones = Calificacion.objects.all().select_related('libro')
        for calificacion in calificaciones:
            print(calificacion.libro.titulo)
        calificaciones_serializer = CalificacionSerializer(calificaciones, many = True)
        return JsonResponse(calificaciones_serializer.data, safe = False)
    
    elif(request.method == 'POST'):
        calificacion_data = JSONParser().parse(request)
        calificacion_serializer = CalificacionSerializer(data = calificacion_data)
        if calificacion_serializer.is_valid():
            calificacion_serializer.save()
            return JsonResponse('Agregado correctamente', safe =False)
        return JsonResponse('Fallo al agregar', safe = False)

    elif(request.method == 'PUT'):
        calificacion_data = JSONParser().parse(request)
        calificacion = Calificacion.objects.get(calificacionId=calificacion_data['calificacionId'])
        calificacion_serializer = AutorSerializer(calificacion, data=calificacion_data)
        if calificacion_serializer.is_valid():
            calificacion_serializer.save()
            return JsonResponse('Actualizado correctamente', safe =False)
        return JsonResponse('Fallo al actualizar', safe = False)

    elif request.method == 'DELETE':
        calificacion = Calificacion.objects.get(calificacionId=id)
        calificacion.delete()
        return JsonResponse('Borrado correctamente', safe = False)
