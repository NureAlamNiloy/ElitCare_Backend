from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DoctorViewset, SpecilizationViewset, DesignationViewset, AvailableTimeViewset, ReviewViewset

router = DefaultRouter()
router.register('doctor', DoctorViewset)
router.register('specilization', SpecilizationViewset)
router.register('designation', DesignationViewset)
router.register('availableTime', AvailableTimeViewset)
router.register('review', ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]





