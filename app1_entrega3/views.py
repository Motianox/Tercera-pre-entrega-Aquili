from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from app1_entrega3.forms import PacienteFormulario, MedicoFormulario, TurnoFormulario
from app1_entrega3.models import Paciente, Medico, Turno

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def medicos(request):
    if request.method == 'POST':
        formulario = MedicoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            medico = Medico(nombre=informacion['nombre'], apellido=informacion['apellido'], profesion=informacion['profesion'], lugar_trabajo=informacion['lugar_trabajo'], numero_matricula=informacion['numero_matricula'])
            medico.save()
            return render(request, 'index.html')
    else:
        formulario = MedicoFormulario()
    return render(request, 'medicos.html', {'formulario':formulario})

def pacientes(request):
    if request.method == 'POST':
        formulario = PacienteFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            paciente = Paciente(nombre=informacion['nombre'], apellido=informacion['apellido'], correo=informacion['correo'], documento=informacion['documento'], necesita_consulta=informacion['necesita_consulta'])
            paciente.save()
            return render(request, 'index.html')
    else:
        formulario = PacienteFormulario()
    return render(request, 'pacientes.html', {'formulario':formulario})

def turnos(request):
    if request.method == 'POST':
        formulario = TurnoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            turno = Turno(nombre=informacion['nombre'], apellido=informacion['apellido'], documento=informacion['documento'], fecha=informacion['fecha'], necesita_medico=informacion['necesita_medico'])
            #turnos con fecha duplicada
            turnos_d = Turno.objects.filter(fecha=informacion['fecha'])
            #medico ingresado por el usuario
            medico = informacion['necesita_medico']
            if not Turno.objects.filter(necesita_medico=medico).exists():
                respuesta = 'No hay ningún médico del tipo ingresado.'
                return render(request, 'turnos.html', {'respuesta': respuesta})
            if turnos_d.count() > 0:
                respuesta = 'Ya hay un turno existente para esa fecha.'
                return render(request, 'turnos.html', {'respuesta': respuesta})
            turno.save()
            return render(request, 'index.html')
    else:
        formulario = TurnoFormulario()
    return render(request, 'turnos.html', {'formulario':formulario})

'''''
if request.GET.get('fecha'):
                fecha = request.GET['fecha']
                if fecha == Medico.objects.filter(fecha__icontains=fecha):
                    mensaje = 'La fecha está ocupada.'
                    return render(request, 'turnos.html', {'mensaje':mensaje})
                else:
'''''

def verMedicos(request):
    if request.GET.get('profesion'):
        profesion = request.GET['profesion']
        medico = Medico.objects.filter(profesion__icontains=profesion)

        return render(request, 'buscarMedicos.html', {'medico':medico, 'profesion':profesion})
    else:
        respuesta = 'No se enviaron datos.'
    return render(request, 'buscarMedicos.html', {'respuesta':respuesta})

