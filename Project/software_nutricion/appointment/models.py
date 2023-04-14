from django.db import models
from datetime import datetime

# Create your models here.
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now)
    observaciones = models.CharField(max_length=200, default="")
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Cita de {} con fecha: {} - {}".format(self.patient.nombre, self.fecha, self.hora)

class Prescription(models.Model):
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    fecha = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now)
    calificacion_seguimiento = models.IntegerField(default=0)
    acoplo = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "Receta de {} con fecha: {} - {}".format(self.appointment.patient, self.fecha, self.hora)
