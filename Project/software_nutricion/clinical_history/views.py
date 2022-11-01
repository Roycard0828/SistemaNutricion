from django.shortcuts import render, redirect
from http.client import HTTPResponse
from django.http import HttpResponse

from .forms import *

def save_form(form, pk):
    clinical_history = ClinicalHistory.objects.get(patient_id=pk)
    formulario = form.save(commit=False)
    formulario.historial_clinico = clinical_history
    formulario.save()
    clinical_history.steps = formulario.step
    clinical_history.save()

# Create your views here.

def clinical_history_view(request):
    form = ClinicalHistoryForm()
    
    if request.method == 'POST':
        form = ClinicalHistoryForm(request.POST)
        if form.is_valid():
            clinical_history = form.save()
            id = clinical_history.patient_id
            return redirect('antecedente_familiar_patologico', pk=id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_familiar_patologico_view(request, pk):
    name = "Antecedente Familiar Patologico"
    form = AntecedenteFamiliarPatologicoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedenteFamiliarPatologicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedente_personal_patologico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_personal_patologico_view(request, pk):
    name = "Antecedente Personal Patologico"
    form = AntecedentePersonalPatologicoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentePersonalPatologicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('historial_psiquiatrico_quirurgico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def historial_psiquiatrico_quirurgico_view(request, pk):
    name = "Historial Psiquiatrico y Quirurgico"
    form = HistorialPsiquiatricoQuirurgicoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = HistorialPsiquiatricoQuirurgicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedente_ginetico_obsetrico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_ginetico_obsetrico_view(request, pk):
    name = "Antecedente Ginetico Obsetrico"
    form = AntecedenteGineticoObsetricoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedenteGineticoObsetricoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('tratamiento', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)
    
def tratamiento_view(request, pk):
    name = "Tratamiento"
    form = TratamientoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('efecto_farmaco_nutricion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def efecto_farmaco_nutricion_view(request, pk):
    name = "Efecto de farmacos en el estado de nutricion"
    form = EfectoFarmacoNutricionForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = EfectoFarmacoNutricionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedente_personal_no_patologico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_personal_no_patologico_view(request, pk):
    name = "Antecedentes personales no patologicos"
    form = AntecedentePersonalNoPatologicoForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentePersonalNoPatologicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('sintomas_actuales', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def sintomas_actuales_view(request, pk):
    name = "Sintomas actuales"
    form = SintomasActualesForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = SintomasActualesForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedentes_clinico_anormales', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedentes_clinico_anormales_view(request, pk):
    name = "Laboratorios clinicos anormales"
    form = AntecedentesClinicoAnormalesForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentesClinicoAnormalesForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedentes_problemas_nutricion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedentes_problemas_nutricion_view(request, pk):
    name = "Antecedentes de problemas relacionados con la nutricion"
    form = AntecedentesProblemasNutricionForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentesProblemasNutricionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('actividad_fisica', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def actividad_fisica_view(request, pk):
    name = "Actividad fisica"
    form = ActividadFisicaForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = ActividadFisicaForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('crono_habitos', pk=clinical_id)
        else:
            return HttpResponse("Something went wrong")

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def crono_habitos_view(request, pk):
    name = "Crono habitos"
    form = CronoHabitosForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = CronoHabitosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('indicadores_dieteticos', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def indicadores_dieteticos_view(request, pk):
    name = "Indicadores dieteticos"
    form = IndicadoresDieteticosForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = IndicadoresDieteticosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('recordatorio_24_horas', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def recordatorio_24_horas_view(request, pk):
    name = "Recordatorio de 24 horas"
    form = Recordatorio24HorasForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = Recordatorio24HorasForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('frecuencia_alimentos', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def frecuencia_alimentos_view(request, pk):
    name = "Frecuencia de alimentos"
    form = FrecuenciaAlimentosForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = FrecuenciaAlimentosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('motivacion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def motivacion_view(request, pk):
    name = "Motivacion"
    form = MotivacionForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = MotivacionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('metas', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)

def metas_view(request, pk):
    name = "Metas"
    form = MetasForm()
    clinical_id = pk 

    if request.method == 'POST':
        form = MetasForm(request.POST)
        if form.is_valid():
            clinical_history = ClinicalHistory.objects.get(patient_id=pk)
            formulario = form.save(commit=False)
            formulario.historial_clinico = clinical_history
            formulario.save()
            clinical_history.finished = True
            clinical_history.steps = formulario.step
            clinical_history.save()
            url = '/patients/patient/{}'.format(clinical_id)
            return redirect(url)
        else:
            return HTTPResponse(status=404)

    context = {'form': form, 'name': name}
    return render(request, 'create_forms/clinical_history_form.html', context)
