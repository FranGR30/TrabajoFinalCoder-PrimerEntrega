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

def agregarPelicula(request):
    if request.method == 'POST':
        miFormulario = Agregar_Pelicula(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pelicula = Pelicula(nombre = informacion['nombre'], fechaEstreno = informacion['fechaEstreno'], duracion = informacion['duracion'])
            pelicula.save()
            return render(request,'App/inicio.html')
    else:
        miFormulario = Agregar_Pelicula()
    return render(request,'App/agregarPelicula.html',{'formulario':miFormulario})

def peliculas(request):
    return render(request,'App/peliculas.html')

def list_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request,'App/peliculas.html',{'peliculas':peliculas})

def buscar(request):
    nombre = request.GET['nombre']
    peliculas = Pelicula.objects.filter(nombre = nombre)
    return render(request,'App/peliculaBuscada.html',{'peliculas':peliculas,'nombre':nombre})    

def comprarEntrada(request):
    if request.method == 'POST':
        miFormulario = ComprarEntradaForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            comprarEntradita = ComprarEntrada(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                telefono=informacion['telefono'],
                pelicula=informacion['pelicula'],
                metodoDePago=informacion['metodoDePago'],
                horario=informacion['horario']
                )
            comprarEntradita.save()
            return render(request,'App/inicio.html')
    peliculas = Pelicula.objects.all()
    return render(request,'App/comprarEntrada.html',{'peliculas':peliculas})
