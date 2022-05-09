from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'App/inicio.html')

def contacto(request):
    if request.method == 'post':
        miFormulario = Contacto(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre = informacion['nombre'],email = informacion['email'],telefono = informacion['telefono'],comentario = informacion['comentario'])
            usuario.save()
            return render(request,'App/inicio.html')
    else:
        miFormulario = Contacto()
    return render(request,'App/contacto.html')