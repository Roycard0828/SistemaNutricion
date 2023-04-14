from django.urls import path
from .views import create_appointment, get_appointments_enabled, update_appointment, get_appointment

urlpatterns = [
    path('create-appointment/<int:pk>', create_appointment, name='create_appointment'),
    path('update-appointment/<int:pk>', update_appointment, name='update_appointment'),
    path('', get_appointments_enabled, name='get_appointments'),
    path('get-appointment/<int:pk>', get_appointment, name='get_appointment'),
]