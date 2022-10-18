from django.contrib import admin
from .models import ClinicalHistory, AntecendenteFamiliarPatologico

# Register your models here.
admin.site.register(ClinicalHistory)
admin.site.register(AntecendenteFamiliarPatologico)