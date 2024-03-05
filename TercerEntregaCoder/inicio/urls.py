from django.urls import path
from inicio.views import inicio, crear_mascota,listado_mascotas


urlpatterns = [
    path('', inicio, name='inicio'),
    path('mascotas/nuevo/', crear_mascota, name='crear_mascota'),
    path('mascotas/listado-mascotas/', listado_mascotas, name='listado_mascotas'),
]