from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaborador

class ColaboradorForm(ModelForm):

    class Meta:
        model = Colaborador
        fields =['rut', 'imagen', 'nombre', 'telefono', 'direccion', 'email', 'pais', 'contraseña']
        labels ={
            'rut': 'Rut', 
            'imagen': 'Imagen', 
            'nombre': 'Nombre',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
            'pais': 'Pais',
            'contraseña': 'Contraseña',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono',
                    'id': 'telefono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese email', 
                    'id': 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese pais', 
                    'id': 'pais'
                }
            ),
            'contraseña': forms.HiddenInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contraseña'
                }
            ),
            

        }