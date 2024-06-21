from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset


router = DefaultRouter() #eita amader main router
router.register(r'service', ServiceViewset, basename='services') # router antena

urlpatterns = [
    path('', include(router.urls)),
]