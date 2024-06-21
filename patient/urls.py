from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset, RegistrationViewset, activate, LoginViewset, LogoutView


router = DefaultRouter() #eita amader main router
router.register('patient', PatientViewset) # router antena
# router.register('register', RegistrationViewset) # router antena

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationViewset.as_view(), name="register"),
    path('login/', LoginViewset.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('active/<uid64>/<token>/', activate, name="activate"),
]