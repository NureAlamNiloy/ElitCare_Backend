from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientModelAdmin(admin.ModelAdmin):
    list_display = ["Username",'FirstName','LastName','phone']

    def Username(self,obj):
        return obj.user.username
    def FirstName(self,obj):
        return obj.user.first_name
    def LastName(self,obj):
        return obj.user.last_name




admin.site.register(Patient, PatientModelAdmin)

