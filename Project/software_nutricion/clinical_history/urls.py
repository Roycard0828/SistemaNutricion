from django.urls import path
from .views import *

urlpatterns = [
    path('create/main', clinical_history_view, name='main_clinical_history'),
    path('create/antecedente-familiar-patologico/<int:pk>', antecedente_familiar_patologico_view, name='antecedente_familiar_patologico'),
    path('create/antecedente-personal-patologico/<int:pk>', antecedente_personal_patologico_view, name='antecedente_personal_patologico'),
    path('create/historial-psiquiatrico-quirurgico/<int:pk>', historial_psiquiatrico_quirurgico_view, name='historial_psiquiatrico_quirurgico'),
    path('create/antecedente-ginetico-obsetrico/<int:pk>', antecedente_ginetico_obsetrico_view, name='antecedente_ginetico_obsetrico'),
    path('create/tratamiento/<int:pk>', tratamiento_view, name='tratamiento'),
    path('create/efecto-farmaco-nutricion/<int:pk>', efecto_farmaco_nutricion_view, name='efecto_farmaco_nutricion'),
    path('create/antecedente-personal-no-patologico/<int:pk>', antecedente_personal_no_patologico_view, name='antecedente_personal_no_patologico'),
    path('create/sintomas-actuales/<int:pk>', sintomas_actuales_view, name='sintomas_actuales'),
    path('create/antecedentes-clinico-anormales/<int:pk>', antecedentes_clinico_anormales_view, name='antecedentes_clinico_anormales'),
    path('create/antecedentes-problemas-nutricion/<int:pk>', antecedentes_problemas_nutricion_view, name='antecedentes_problemas_nutricion'),
    path('create/actividad-fisica/<int:pk>', actividad_fisica_view, name='actividad_fisica'),
    path('create/crono-habitos/<int:pk>', crono_habitos_view, name='crono_habitos'),
    path('create/indicadores-dieteticos/<int:pk>', indicadores_dieteticos_view, name='indicadores_dieteticos'),
    path('create/recordatorio-24_horas/<int:pk>', recordatorio_24_horas_view, name='recordatorio_24_horas'),
    path('create/frecuencia-alimentos/<int:pk>', frecuencia_alimentos_view, name='frecuencia_alimentos'),
    path('create/motivacion/<int:pk>', motivacion_view, name='motivacion'),
    path('create/metas/<int:pk>', metas_view, name='metas')
]