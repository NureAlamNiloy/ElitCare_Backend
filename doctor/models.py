from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.


class Specilization(models.Model):
    name = models.CharField(max_length= 40)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length= 40)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length= 40)
    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor/")
    specilization = models.ManyToManyField(Specilization)
    designation = models.ManyToManyField(Designation)
    availableTime = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    link = models.URLField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
StarChoice = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
]
class review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=7, choices=StarChoice) 

    def __str__(self):
        return f"Patient: {self.reviewer.user.first_name}  Reviewed  D. {self.doctor.user.first_name}"
    