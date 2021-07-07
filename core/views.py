from core.forms import ColaboradorForm
from django.shortcuts import redirect, render
from .models import Colaborador
# Create your views here.

def home(request):
    colaboradores = Colaborador.objects.all()
    data = {
        'colaborador': Colaborador.objects.all()
    }
    return render(request, 'home.html', data)

def colaborador(request):
    if request.method=='POST': 
        colaborador_form = ColaboradorForm(request.POST, files=request.FILES)
        if colaborador_form.is_valid():
            pepe = colaborador_form.save(commit=False)
            pepe.contraseña = password(pepe.rut, pepe.nombre, pepe.pais, pepe.telefono)
            pepe.save()
            return redirect('home')
    else:
        colaborador_form= ColaboradorForm()
    return render(request, 'colaborador.html', {'colaborador_form': colaborador_form})


def vercolaborador(request):
    colaboradores = Colaborador.objects.all()
    datos = {
        'colaboradores': colaboradores
    }
    return render(request, 'vercolaborador.html', datos)

def form_mod_colaborador(request,id):
    colaborador = Colaborador.objects.get(rut=id)

    datos ={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST, instance = colaborador, files=request.FILES)
        if formulario.is_valid: 
            colaborador.delete()
            pepe = formulario.save(commit = False)
            pepe.contraseña = password(pepe.rut, pepe.nombre, pepe.pais, pepe.telefono)
            pepe.save()    
            return redirect('vercolaborador')
    return render(request, 'form_mod_colaborador.html', datos)

def form_del_colaborador(request,id):
    colaborador = Colaborador.objects.get(rut=id)
    colaborador.delete()
    return redirect('vercolaborador')

def password(dato1, dato2, dato3, dato4):
    subcadena1 = str(dato1) [:2]
    subcadena2 = dato2 [:2]
    subcadena3= subcadena2.upper()
    subcadena4 = dato3[-2:]
    subcadena5 = subcadena4.lower()
    subcadena6 = str(dato4)[-2:]
    contraseña= subcadena1+subcadena3+subcadena5+subcadena6
    return contraseña
