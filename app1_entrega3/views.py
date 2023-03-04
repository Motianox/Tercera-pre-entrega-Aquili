from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def verMedicos(request):
    return render(request, 'verMedicos.html')

def medicos(request):
    return render(request, 'medicos.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def turnos(request):
    return render(request, 'turnos.html')