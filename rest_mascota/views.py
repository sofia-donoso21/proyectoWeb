from django.shortcuts import render
from rest_framework import status
from rest_framework import response
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from appWeb.models import Mascotas
from .serializers import MascotasSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def lista_mascotas(request):
    #Lista de todas las mascotas

    if request.method == 'GET':
        mascota = Mascotas.objects.all()
        serializer = MascotasSerializer(mascota, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_mascota(request, codigo):
    #Obtener los datos según llave
    try:
        mascota = Mascotas.objects.get(codigo=codigo)
    except Mascotas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #Obtener detalle del registro encontrado
    if request.method == 'GET':
        serializer = MascotasSerializer(mascota)
        return Response(serializer.data)

    #Modificar datos del registro encontrado
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MascotasSerializer(mascota, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Eliminar registro encontrado
    if request.method == 'DELETE':
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

