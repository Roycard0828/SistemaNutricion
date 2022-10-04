from django.urls import path
from .views import create_patient, get_patient, delete_patient, update_patient, get_all_patients

urlpatterns = [
    path('create/', create_patient, name='create_patient'),
    path('patient/<int:pk>', get_patient, name='get_patient'),
    path('delete/<int:pk>', delete_patient, name='delete_patient'),
    path('', get_all_patients, name='patients'),
    path('update_patient/<int:pk>', update_patient, name='update_patient'),
]