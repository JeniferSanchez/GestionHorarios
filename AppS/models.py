from django.db import models

class coordinador(models.Model):
    coor_cedula=models.IntegerField(primary_key=True)
    coor_nombre=models.CharField(max_length=30)
    coor_apellido=models.CharField(max_length=45)
    coor_correo=models.CharField(max_length=30)
    coor_telefono=models.CharField(max_length=10)

class docente(models.Model):
    doc_cedula=models.IntegerField(primary_key=True)
    doc_nombre=models.CharField(max_length=30)
    doc_apellido=models.CharField(max_length=45)
    doc_correo=models.CharField(max_length=30)
    doc_telefono=models.CharField(max_length=10)

class Horario(models.Model):
    hor_codigo=models.AutoField(primary_key=True)
    hor_fechaInicio=models.DateField
    hor_fechaFin=models.DateField
    hor_horaInicio=models.TimeField
    horhoraFin=models.TimeField
    coor_cedula=models.ForeignKey(coordinador, on_delete=models.CASCADE)

class usuario(models.Model):
    user_cedula=models.IntegerField(primary_key=True)
    user_nombre=models.CharField(max_length=30)
    user_apellido=models.CharField(max_length=45)
    user_correo=models.CharField(max_length=30)
    user_clave=models.CharField(max_length=30)
    user_rol=models.CharField(max_length=11)
    user_usuario=models.CharField(max_length=30)
