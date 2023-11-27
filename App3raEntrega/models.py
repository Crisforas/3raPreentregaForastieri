from django.db import models

# Create your models here.
class Lista_Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField(int)
    email = models.EmailField(max_length=40, unique=True)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.pais}, Edad: {self.edad}, Email: {self.email}"

class Consumible(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    cantidad = models.IntegerField(int)

    def __str__(self):
        return  f"Nombre: {self.nombre}, Marca: {self.marca}, Modelo: {self.modelo}, Cantidad: {self.cantidad}"


class Servicio(models.Model):
    paciente = models.CharField(max_length=40)
    trabajo = models.CharField(max_length=40)
    precio = models.IntegerField(int)


    def __str__(self):
        return f"Paciente: {self.ortodoncia}, Trabajo: {self.trabajo}, Precio: {self.precio}"





