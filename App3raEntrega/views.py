from django.http import HttpResponse
from django.shortcuts import render

from App3raEntrega.models import Lista_Paciente, Consumible, Servicio


# Create your views here.

def mostrar_paciente(request):
    pacientes = Lista_Paciente.objects.all()
    contexto = {
        "pacientes": pacientes
    }
    return render(request, "App3raEntrega/pacientes.html", contexto)


def ingresar_paciente(request):
    paciente = Lista_Paciente(nombre="", apellido="", edad="", email="")
    paciente.save()
    contexto = {"paciente": paciente}

    return HttpResponse(f" El paciente {paciente.nombre}{paciente.apellido} tiene {paciente.edad}")

def ingresar_consumible(request):
    consumible = Consumible(nombre="", marca="", modelo="", cantidad="")
    consumible.save()
    contexto = {"consumible": consumible}

    return HttpResponse(f" Hay {consumible.cantidad} de {consumible.nombre}{consumible.marca}{consumible.modelo}")

def trabajo_realizado(request):
    trabajo = Servicio(paciente="", trabajo="", precio="")
    trabajo.save()
    contexto = {"trabajo": trabajo}

    return HttpResponse(f"Al paciente {trabajo.paciente} se le realizo {trabajo.trabajo} y costo {trabajo.precio}")

def show_html(request):
    pacientes = Lista_Paciente.objects.first()
    contexto = {"nombre": "Cris"}
    return render(request, 'index.html', contexto)

