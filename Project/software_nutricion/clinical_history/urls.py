from django.urls import path
from .views import create_clinical_history

urlpatterns = [
    path('create/', create_clinical_history, name='create'),
]