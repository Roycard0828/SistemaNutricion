from django.forms import ModelForm
from .models import *

class ClinicalHistoryForm(ModelForm):

    class Meta:
        model = ClinicalHistory
        fields = '__all__'
        labels = {
            "motivo_consulta": "Motivo de consulta",
            "dx_medico": "DX Medico",
            "estado_salud": "Estado de Salud"
        }

class AntecedenteFamiliarPatologicoForm(ModelForm):

    class Meta:
        model = AntecendenteFamiliarPatologico
        fields = '__all__'
        labels = {
            "paterno": "Antecedente paterno",
            "materno": "Antecedente materno",
        }

class AntecedentePersonalPatologicoForm(ModelForm):
    class Meta:
        model = AntecedentePersonalPatologico
        fields = '__all__'
        labels = {
            "enfermedades_infeccionas": "Enfermedades infecciosas",
            "enfermedades_cronicas": "Enfermedades cronicas",
            "intoleracia_glucosa": "Intolerancia a la glucosa",
            "enfermedades_cardiacas_cronarias": "Enfermedades cardiacas o cronarias",
            "osteoartritis": "Osteoartritis",
            "enfermedades_vesiculares_hepaticas": "Enfermedades vesiculares y hepaticas. ¿Cuales?"
        }

