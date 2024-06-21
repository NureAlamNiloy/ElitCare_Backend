from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', "patient", "appointment_type", "appointment_status", "time"]

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_type ==  "Online" and obj.appointment_status == "Running":
            email_subject = "Your Online Appointment is running"
            email_body = render_to_string("appointment.html", {"user" : obj.patient.user, "doctor":obj.doctor})

            email = EmailMultiAlternatives(email_subject, " ", to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()



admin.site.register(Appointment, AppointmentAdmin)
