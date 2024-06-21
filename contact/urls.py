from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewset


router = DefaultRouter() #eita amader main router
router.register(r'contact', ContactViewset, basename='contactus') # router antena

urlpatterns = [
    path('', include(router.urls)),
]