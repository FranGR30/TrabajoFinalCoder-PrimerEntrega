from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Usuario)
admin.site.register(Cartelera)
admin.site.register(ComprarEntrada)