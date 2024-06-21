from rest_framework import serializers
from .models import Doctor, Specilization, Designation, AvailableTime, review

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    designation = serializers.StringRelatedField(many = True)
    specilization = serializers.StringRelatedField(many = True)
    availableTime = serializers.StringRelatedField(many = True)
    
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