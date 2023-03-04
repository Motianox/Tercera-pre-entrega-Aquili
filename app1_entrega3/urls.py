from django.urls import path, include
from app1_entrega3 import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('verMedicos/', views.verMedicos, name='verMedicos'),
    path('pacientes/', views.pacientes, name='Pacientes'),
    path('turnos/', views.turnos, name='Turnos'),
    path('medicos/', views.medicos, name='Medicos'),
]