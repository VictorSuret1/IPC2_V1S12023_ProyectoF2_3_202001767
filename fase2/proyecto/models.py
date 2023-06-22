from django.db import models

# Create your models here.

class Usuario(models.Model):
    rol = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)
    contrasena = models.TextField()

class Pelicula(models.Model):
    categoria =models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    anio = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

class Salas(models.Model):
    cine = models.CharField(max_length=100)
    numero = models.IntegerField()
    asientos = models.IntegerField()