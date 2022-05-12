from django import forms
from .models import *

metodos_de_pago = [
    ('Visa','Visa'),
    ('Master Card','Master Card'),
    ('American Express','American Express'),
    ('Mercado Pago','Mercado Pago'),
]

def nombrePeliculas ():
    lista_peliculas = []
    for i in Pelicula.nombre:
        lista_peliculas.append(i)
    return lista_peliculas

class Contacto(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    comentario = forms.CharField(max_length=300)

class Agregar_Pelicula(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEstreno = forms.DateField()
    duracion = forms.IntegerField()

class ComprarEntradaForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    pelicula = forms.CharField(max_length=30)
    metodoDePago = forms.CharField(max_length=30)

#label = 'Metodo de pago:',widget = forms.Select(choices = metodos_de_pago)