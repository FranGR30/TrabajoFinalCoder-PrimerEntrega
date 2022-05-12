from django.db import models
from django.db.models import Model
import datetime
import os

# Create your models here.
def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" , (timeNow,old_filename)
    return os.path.join('uploads/',filename)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEstreno = models.DateField()
    duracion = models.IntegerField()
    diasEnPantalla = models.IntegerField
    poster = models.ImageField

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

class ComprarEntrada(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    pelicula = models.CharField(max_length=30)
    metodoDePago = models.CharField(max_length=30)
    horario = models.TimeField()


    
