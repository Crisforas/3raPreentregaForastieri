from django.http import HttpResponse
from django.shortcuts import render

from App3raEntrega.models import Club


# Create your views here.
def ingresar_club(request):
    club = Club(nombre="BocaJrs", division="Primera_A", pais="Argentina")
    club.save()
    contexto = {"club": club}

    return HttpResponse(f" El club {club.nombre} es de {club.division}")

def show_html(request):
    clubs = Club.objects.first()
    contexto = {"nombre": "Cris", "club": clubs}
    return render(request, 'index.html', contexto)

