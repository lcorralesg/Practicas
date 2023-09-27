from django.contrib import admin

# Register your models here.

from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'ciclo', 'telefono')