from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Specilization, Designation, AvailableTime, review
from .serializers import DoctorSerializer, ReviewSerializer, SpecilizationSerializer, DesignationSerializer, AvailableTimeSerializer

# Create your views here.

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class SpecilizationViewset(viewsets.ModelViewSet):
    queryset = Specilization.objects.all()
    serializer_class = SpecilizationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

class ReviewViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    

