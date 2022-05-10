from django.db import models
from django.db.models import Model

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEstreno = models.DateField()
    duracion = models.IntegerField()
    diasEnPantalla = models.DateField
    poster = models.ImageField(null = True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    comentario = models.CharField(max_length=300)

class Cartelera(models.Model):
    pelicula = models.CharField(max_length=30)
    codigoPelicula = models.CharField(max_length=30)
    dia = models.DateField()
    horario = models.TimeField()
    
