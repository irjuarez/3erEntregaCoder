from http.client import HTTPResponse
from datetime import datetime # ejempoo de mostrar Horario

from django.shortcuts import render, redirect
from django.http import HttpResponse # entiende string
from django.template import Template, Context, loader
from inicio.models import Mascota
from inicio.forms import FormularioCreacionMascota


def inicio(request): #1er parametro siempre tiene que ser el request
    return render(request, 'inicio.html', {})

def listado_mascotas(request):
    masc = Mascota.objects.all()
    return render(request, 'mascotas.html', {'mascotas':masc})


def crear_mascota(request):
    formulario=FormularioCreacionMascota()
    if request.method == "POST":   
        formulario = FormularioCreacionMascota(request.POST)
        if formulario.is_valid():
            nombre= formulario.cleaned_data.get('nombre')
            fecha_nacimiento= formulario.cleaned_data.get('fecha_nacimiento')
            raza= formulario.cleaned_data.get('raza')
            color= formulario.cleaned_data.get('color')
            nombre_Dueno= formulario.cleaned_data.get('nombre_Dueno')
            tel_contacto = formulario.cleaned_data.get('tel_contacto')
            mascota = Mascota(nombre=nombre, fecha_nacimiento=fecha_nacimiento , raza=raza, color = color,  nombre_Dueno = nombre_Dueno, tel_contacto = tel_contacto)
            mascota.save()
            return redirect("listado_mascotas")
    
    
    return render(request, 'crear_mascota.html', {'formulario': formulario})