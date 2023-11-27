from django.http import HttpResponse
from django.shortcuts import render

from App3raEntrega.models import Club


# Create your views here.
def ingresar_club(request):
    club = Club(nombre="BocaJrs", division="Primera_A", pais="Argentina")
    club.save()

    return HttpResponse(f"{club.nombre}es el mas grande de )

