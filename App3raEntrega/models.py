from django.db import models

# Create your models here.
class Liga(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=30)

    def __str__(self):
        return f"Liga: {self.nombre}, Pais: {self.pais}"

class Club(models.Model):
    nombre = models.CharField(max_length=40)
    division = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)

    def __str__(self):
        return  f"Nombre: {self.nombre}, Division: {self.division}, Pais: {self.pais}"


class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Nacionalidad: {self.nacionalidad}, Edad: {self.edad}, Posiscion: {self.posicion}"





