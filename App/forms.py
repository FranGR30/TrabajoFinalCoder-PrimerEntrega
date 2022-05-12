from django import forms


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
    horario = forms.TimeField()