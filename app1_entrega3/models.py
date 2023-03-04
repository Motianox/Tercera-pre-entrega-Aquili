from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    profesion = models.CharField(max_length=30)
    numero_matricula = models.IntegerField()
    lugar_trabajo = models.CharField(max_length=50)

class Paciente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    correo = models.EmailField()
    documento = models.IntegerField()
    necesita_consulta = models.BooleanField()

class Turno(models.Model):
    fecha = models.DateField()
    necesita_medico = models.CharField(max_length=30)


