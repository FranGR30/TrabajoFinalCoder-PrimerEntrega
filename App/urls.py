from .views import *
from django.urls import path

urlpatterns = [
     path('',inicio,name='inicio'),
     path('contacto/',contacto,name='contacto'),
     path('peliculas/',list_peliculas,name='peliculas'),
     path('peliculas/',mostrar_pelicula),
]