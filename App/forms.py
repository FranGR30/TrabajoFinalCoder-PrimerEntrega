from django import forms

class Contacto(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    comentario = forms.CharField(max_length=300)