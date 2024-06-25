from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import render
from rest_framework import viewsets, filters, pagination
from .models import Doctor, Specilization, Designation, AvailableTime, review
from .serializers import DoctorSerializer, ReviewSerializer, SpecilizationSerializer, DesignationSerializer, AvailableTimeSerializer

# Create your views here.

class DoctorsPagination(pagination.PageNumberPagination):
    page_size = 1 # Items in per page
    page_size_query_param = 'page_size'
    max_page_size = 200


class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorsPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'user__first_name'] 

class SpecilizationViewset(viewsets.ModelViewSet):
    queryset = Specilization.objects.all()
    serializer_class = SpecilizationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeDoctors(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeDoctors]

class ReviewViewset(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = review.objects.all()
    serializer_class = ReviewSerializer
    



