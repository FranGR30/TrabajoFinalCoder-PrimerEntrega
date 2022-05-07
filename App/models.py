from django.db import models

# Create your models here.
class pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEstreno = models.DateField
    duracion = models.IntegerField()
    diasEnPantalla = models.DateField

class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()

