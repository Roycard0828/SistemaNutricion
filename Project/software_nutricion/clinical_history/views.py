from django.shortcuts import render, redirect
from http.client import OK, HTTPResponse

from .forms import ClinicalHistoryForm, AntecedenteFamiliarPatologicoForm, ClinicalHistory
# Create your views here.

def clinical_history_view(request):
    form = ClinicalHistoryForm()

    if request.method == 'POST':
        form = ClinicalHistoryForm(request.POST)
        if form.is_valid():
            clinical_history = form.save()
            return redirect('antecedente_familiar_patologico', pk=clinical_history.paciente_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_familiar_patologico_view(request, pk):
    form = AntecedenteFamiliarPatologicoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedenteFamiliarPatologicoForm(request.POST)
        if form.is_valid():
            clinical_history = ClinicalHistoryForm.objects.get(paciente_id=pk)
            antecedente_familia_patologico = form.save(commit=False)
            antecedente_familia_patologico.historial_clinico = clinical_history
            antecedente_familia_patologico.save()
            return redirect('')
        else:
            return HTTPResponse(status=404)

    context = {'form': form}
    return render(request, 'create_forms/clinical_history_form.html', context)