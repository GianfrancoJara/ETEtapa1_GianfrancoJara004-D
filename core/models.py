from django.db import models

# Create your models here.

# Modelo de Noticia

class Colaborador(models.Model): 
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='ID Noticia')
    imagen = models.ImageField(null=True, blank=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    direccion = models.CharField(max_length=40, verbose_name='Direccion')
    email = models.CharField(max_length=40, verbose_name='Email')
    pais = models.CharField(max_length=40, verbose_name='Pais')
    contraseña = models.CharField(max_length=100, null=True, blank=True, verbose_name='Contraseña')

    def __str__(self):
        return self.rut



