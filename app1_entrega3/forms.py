from django import forms

class PacienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    correo = forms.EmailField()
    documento = forms.IntegerField()
    necesita_consulta = forms.BooleanField()

class MedicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    profesion = forms.CharField(max_length=30)
    lugar_trabajo = forms.CharField(max_length=30)
    numero_matricula = forms.IntegerField()

class TurnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    documento = forms.IntegerField()
    fecha = forms.DateField()
    necesita_medico = forms.CharField(max_length=30)