from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    edad = models.BigIntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "Paciente con nombre" + self.nombre
    
    class Meta:
        ordering = ['-created']
        