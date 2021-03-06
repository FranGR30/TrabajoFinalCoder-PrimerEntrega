from .views import *
from django.urls import path

urlpatterns = [
     path('',inicio,name='inicio'),
     path('contacto/',contacto,name='contacto'),
     path('peliculas/',list_peliculas,name='peliculas'),
     path('buscar/',buscar, name = 'resultadoBusqueda'),
     path('agregarPelicula/',agregarPelicula, name = 'agregarPelicula'),
     path('comprarEntrada/',comprarEntrada, name = 'comprarEntrada'),
]