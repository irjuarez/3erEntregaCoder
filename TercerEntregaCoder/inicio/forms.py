from socket import fromshare
from django import forms

class FormularioCreacionMascota(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_nacimiento = forms.CharField(max_length=20)
    raza = forms.CharField(max_length=20)
    color = forms.CharField(max_length=15)
    nombre_Dueno = forms.CharField(max_length=50)
    tel_contacto = forms.CharField(max_length=20)
