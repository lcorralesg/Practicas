from django.shortcuts import render, redirect
from .models import Alumno

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})

def guardar_alumno(request):
    if request.method == 'POST':
        nombre = request.POST['txtnombre']
        apellido = request.POST['txtapellido']
        correo = request.POST['txtcorreo']
        ciclo = request.POST['txtciclo']
        telefono = request.POST['txttelefono']
        alumno = Alumno(nombre=nombre, apellido=apellido, correo=correo, ciclo=ciclo, telefono=telefono)
        alumno.save()
        return redirect('Alumnos:index')
    else:
        return redirect('Alumnos:index')
