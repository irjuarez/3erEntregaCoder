from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_nacimiento = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    nombre_Dueno = models.CharField(max_length=50)
    tel_contacto = models.CharField(max_length=20)
    
    def __str__(self):
        return f"  Nombre: {self.nombre} \n - Fecha Nacimiento: {self.fecha_nacimiento} \n - Raza: {self.raza} \n - Color: {self.color} \n - Dueño: {self.nombre_Dueno} \n - Tel. Contacto: {self.tel_contacto} \n"
    



        