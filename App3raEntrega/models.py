from django.db import models

# Create your models here.
class Liga(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)

class Club(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=20)





