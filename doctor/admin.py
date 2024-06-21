from django.contrib import admin
from .models import Specilization, AvailableTime, Designation, Doctor, review

# Register your models here.

class SpecilizationModelAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('name',),}

class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('name',),}

admin.site.register(Specilization, SpecilizationModelAdmin)
admin.site.register(AvailableTime)
admin.site.register(Designation, DesignationModelAdmin)
admin.site.register(Doctor)
admin.site.register(review)

