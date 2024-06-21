from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.

Appointment_Type = [
    ('Online','Online'),
    ('Offline','Offline')
]
Appointment_Status = [
    ('Panding','Panding'),
    ('Running','Running'),
    ('Complete','Complete')
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=Appointment_Type, max_length=20)
    appointment_status = models.CharField(choices=Appointment_Status, max_length=20, default="Panding")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default= False)

    def __str__(self):
        return f"D. {self.doctor.user.first_name}, Paitent: {self.patient.user.first_name}"
    