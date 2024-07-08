from rest_framework import serializers
from .models import Doctor, Specilization, Designation, AvailableTime, review
from django.contrib.auth.models import User

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    designation = serializers.PrimaryKeyRelatedField(queryset=Designation.objects.all(), many=True)
    specilization = serializers.PrimaryKeyRelatedField(queryset=Specilization.objects.all(), many=True)
    availableTime = serializers.PrimaryKeyRelatedField(queryset=AvailableTime.objects.all(), many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class SpecilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specilization
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'