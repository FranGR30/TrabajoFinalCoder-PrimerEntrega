from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'App/inicio.html')

def contacto(request):
    if request.method == 'POST':
        miFormulario = Contacto(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre = informacion['nombre'],email = informacion['email'],telefono = informacion['telefono'],comentario = informacion['comentario'])
            usuario.save()
            return render(request,'App/inicio.html')
    else:
        miFormulario = Contacto()
    return render(request,'App/contacto.html',{'formulario':miFormulario})

def peliculas(request):
    return render(request,'App/peliculas.html')

def list_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request,'App/peliculas.html',{'peliculas':peliculas})

def mostrar_pelicula(request):
    #if request.GET['nombre']:
    nombre = request.GET['nombre']
    #    pelicula = Pelicula.objects.filter(nombre = nombre)
    return render(request,'App/peliculas.html',{'nombre':nombre})    
    #else:
    #    respuesta = 'a'
    #return render(request,'App/peliculas.html',{'respuesta':respuesta})
