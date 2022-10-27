from django.urls import path
from .views import clinical_history_view, antecedente_familiar_patologico_view

urlpatterns = [
    path('create/main', clinical_history_view, name='main_clinical_history'),
    path('create/antecedente-familiar-patologico/<int:pk>', antecedente_familiar_patologico_view, name='antecedente_familiar_patologico'),
]