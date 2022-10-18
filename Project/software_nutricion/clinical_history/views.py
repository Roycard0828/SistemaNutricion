from django.shortcuts import render, redirect

from .forms import ClinicalHistoryForm, AntecendenteFamiliarPatologicoForm
# Create your views here.

def create_clinical_history(request):
    form = ClinicalHistoryForm()
    antecedentes_familiares_form = AntecendenteFamiliarPatologicoForm()

    context = {
        'form': form,
        'antecedentes_familiares_form': antecedentes_familiares_form 
    }

    return render(request, 'clinical_history_form.html', context)