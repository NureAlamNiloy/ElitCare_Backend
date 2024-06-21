from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactSerilizers

# Create your views here.


class ContactViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerilizers
