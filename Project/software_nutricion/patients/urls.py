from django.urls import path
from .views import create_patient, get_patient

urlpatterns = [
    path('create/', create_patient, name='create'),
    path('patient/<int:pk>', get_patient, name='get_patient'),
]