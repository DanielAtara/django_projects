from django.db import models

# Create your models here.
class rol(models.Model):
    nombre_rol = models.CharField(max_length=100)
    descripcion_rol = models.CharField(max_length=100)
    
class desarrolador(models.Model):
    nombre_desarrolador = models.CharField(max_length=100)
    apellido_desarrolador = models.CharField(max_length=100)
    rol_desarrolador = models.ForeignKey(rol, on_delete=models.CASCADE)
    
class tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    desarrolador_tasks = models.ForeignKey(desarrolador, on_delete=models.CASCADE )