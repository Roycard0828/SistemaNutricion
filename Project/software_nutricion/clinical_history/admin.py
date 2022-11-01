from django.contrib import admin
from .models import *  

# Register your models here.
admin.site.register(ClinicalHistory)
admin.site.register(AntecendenteFamiliarPatologico)
admin.site.register(AntecedentePersonalPatologico)
admin.site.register(HistorialPsiquiatricoQuirurgico)
admin.site.register(AntecedenteGineticoObsetrico)
admin.site.register(Tratamiento)
admin.site.register(ActividadFisica)