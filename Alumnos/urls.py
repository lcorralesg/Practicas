from django.urls import path
from . import views

app_name = 'Alumnos'

urlpatterns = [
    path('', views.index, name='index'),
    path('guardar_alumno', views.guardar_alumno, name='guardar_alumno'),
]