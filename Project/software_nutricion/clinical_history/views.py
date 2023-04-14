from django.shortcuts import render, redirect
from http.client import HTTPResponse
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
# from xhtml2pdf import pisa

from .forms import *

def save_form(form, pk):
    #Guardar las pasos del historial y vincularlos con el historial clinico
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
            return HttpResponse(status=404)

    context = {'form': form}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_familiar_patologico_view(request, pk):
    name = "Antecedente Familiar Patologico"
    form = AntecedenteFamiliarPatologicoForm()
    clinical_id = pk 

    if request.method == 'POST':    
        form = AntecedenteFamiliarPatologicoForm(data=request.POST, update=False)        
        if form.is_valid():            
            save_form(form, clinical_id)            
            return redirect('antecedente_personal_patologico', pk=clinical_id)
        else:           
            return HttpResponse(status=404)
    
    elif request.method == 'GET':
        try:
            #Update the data
            instance = AntecedenteFamiliarPatologico.objects.get(pk=clinical_id)
            form = AntecedenteFamiliarPatologicoForm(update=True, instance=instance)
            action = "update"
        except:
            action = "create"
        
    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_personal_patologico_view(request, pk):
    name = "Antecedente Personal Patologico"
    clinical_id = pk

    if request.method == 'POST':
        form = AntecedentePersonalPatologicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('historial_psiquiatrico_quirurgico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = AntecedentePersonalPatologico.objects.get(pk=clinical_id)
            form = AntecedentePersonalPatologicoForm(update=True, instance=instance)
            action = "update"
        except:
            action = "create"
            form = AntecedentePersonalPatologicoForm()            
    
    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def historial_psiquiatrico_quirurgico_view(request, pk):
    name = "Historial Psiquiatrico y Quirurgico"    
    clinical_id = pk

    if request.method == 'POST':
        form = HistorialPsiquiatricoQuirurgicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedente_ginetico_obsetrico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)
    
    elif request.method == 'GET':
        try:
            instance = HistorialPsiquiatricoQuirurgico.objects.get(pk+clinical_id)
            form = HistorialPsiquiatricoQuirurgicoForm(update=True, instance=instance)
            action = "update"
        except:
            form = HistorialPsiquiatricoQuirurgicoForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
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
    elif request.method == 'GET':
        try:            
            instance = AntecedenteGineticoObsetrico.objects.get(pk=pk)
            form = AntecedenteGineticoObsetricoForm(instance=instance, update_mood=True)
            action = "update"
        except:
            form = AntecedenteGineticoObsetricoForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)
    
def tratamiento_view(request, pk):
    name = "Tratamiento"
    clinical_id = pk 

    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('efecto_farmaco_nutricion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = Tratamiento.objects.get(pk=clinical_id)
            form = TratamientoForm(update=True, instance=instance)
            action = "update"
        except:
            form = TratamientoForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def efecto_farmaco_nutricion_view(request, pk):
    name = "Efecto de farmacos en el estado de nutricion"
    clinical_id = pk 

    if request.method == 'POST':
        form = EfectoFarmacoNutricionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedente_personal_no_patologico', pk=clinical_id)
        else:
            return HTTPResponse(status=404)
    
    elif request.method == 'GET':
        try:
            instance = EfectoFarmacoNutricion.objects.get(pk=clinical_id)
            form = EfectoFarmacoNutricionForm(update=True, instance=instance)
            action = "update"
        except:
            form = EfectoFarmacoNutricionForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedente_personal_no_patologico_view(request, pk):
    name = "Antecedentes personales no patologicos"
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentePersonalNoPatologicoForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('sintomas_actuales', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = AntecedentePersonalNoPatologico.objects.get(pk=clinical_id)
            form = AntecedentePersonalNoPatologicoForm(update=True, instance=instance)
            action = "update"
        except:
            form = AntecedentePersonalNoPatologicoForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def sintomas_actuales_view(request, pk):
    name = "Sintomas actuales"
    clinical_id = pk 

    if request.method == 'POST':
        form = SintomasActualesForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedentes_clinico_anormales', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = SintomasActuales.objects.get(pk=clinical_id)
            form = SintomasActualesForm(update=True, instance=instance)
            action = "update"
        except:
            form = SintomasActualesForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedentes_clinico_anormales_view(request, pk):
    name = "Laboratorios clinicos anormales"
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentesClinicoAnormalesForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('antecedentes_problemas_nutricion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)
    
    elif request.method == 'GET':
        try:
            instance = AntecedentesClinicoAnormales.objects.get(pk=clinical_id)
            form = AntecedentesClinicoAnormalesForm(update=True, instance=instance)
            action = "update"
        except:
            form = AntecedentesClinicoAnormalesForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def antecedentes_problemas_nutricion_view(request, pk):
    name = "Antecedentes de problemas relacionados con la nutricion"
    clinical_id = pk 

    if request.method == 'POST':
        form = AntecedentesProblemasNutricionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('actividad_fisica', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = AntecedentesProblemasNutricion.objects.get(pk=clinical_id)
            form = AntecedentesProblemasNutricionForm(update=True, instance=instance)
            action = "update"
        except:
            form = AntecedentesProblemasNutricionForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def actividad_fisica_view(request, pk):
    name = "Actividad fisica"
    clinical_id = pk 

    if request.method == 'POST':
        form = ActividadFisicaForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('crono_habitos', pk=clinical_id)
        else:
            return HttpResponse("Something went wrong")

    elif request.method == 'GET':
        try:
            instance = ActividadFisica.objects.get(pk=clinical_id)
            form = ActividadFisicaForm(update=True, instance=instance)
            action = "update"
        except:
            form = ActividadFisicaForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def crono_habitos_view(request, pk):
    name = "Crono habitos"
    clinical_id = pk 

    if request.method == 'POST':
        form = CronoHabitosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('indicadores_dieteticos', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = CronoHabitos.objects.get(pk=clinical_id)
            form = CronoHabitosForm(update=True, instance=instance)
            action = "update"
        except:
            form = CronoHabitosForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def indicadores_dieteticos_view(request, pk):
    name = "Indicadores dieteticos"
    clinical_id = pk 

    if request.method == 'POST':
        form = IndicadoresDieteticosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('recordatorio_24_horas', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = IndicadoresDieteticos.objects.get(pk=clinical_id)
            form = IndicadoresDieteticosForm(update=True, instance=instance)
            action = "update"
        except:
            form = IndicadoresDieteticosForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def recordatorio_24_horas_view(request, pk):
    name = "Recordatorio de 24 horas"
    clinical_id = pk 

    if request.method == 'POST':
        form = Recordatorio24HorasForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('frecuencia_alimentos', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = Recordatorio24Horas.objects.get(pk=clinical_id)
            form = Recordatorio24HorasForm(update=True, instance=instance)
            action = "update"
        except:
            form = Recordatorio24HorasForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def frecuencia_alimentos_view(request, pk):
    name = "Frecuencia de alimentos"
    clinical_id = pk 

    if request.method == 'POST':
        form = FrecuenciaAlimentosForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('motivacion', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            instance = FrecuenciaAlimentos.objects.get(pk=clinical_id)
            form = FrecuenciaAlimentosForm(update=True, instance=instance)
            action = "update"
        except:
            form = FrecuenciaAlimentosForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def motivacion_view(request, pk):
    name = "Motivacion"
    clinical_id = pk 

    if request.method == 'POST':
        form = MotivacionForm(request.POST)
        if form.is_valid():
            save_form(form, clinical_id)
            return redirect('metas', pk=clinical_id)
        else:
            return HTTPResponse(status=404)

    elif request.method == 'GET':
        try:
            # 
            instance = Motivacion.objects.get(pk=clinical_id)
            form = MotivacionForm(update=True, instance=instance)
            action = "update"
        except:
            form = MotivacionForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def metas_view(request, pk):
    name = "Metas"
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
    
    elif request.method == 'GET':
        try:
            instance = Metas.objects.get(pk=clinical_id)
            form = MetasForm(update=True, instance=instance)
            action = "update"
        except:
            form = MetasForm()
            action = "create"

    context = {'form': form, 'name': name, 'action': action}
    return render(request, 'create_forms/clinical_history_form.html', context)

def clinical_history_format_view(request, pk):
    
    clinical_history = ClinicalHistory.objects.get(pk=pk)

    clinical_history_form = ClinicalHistoryForm(instance=clinical_history)
    antecedente_familiar_patologico_form = AntecedenteFamiliarPatologicoForm(instance=clinical_history.antecedentefamiliarpatologico)
    antecedente_personal_patologico_form = AntecedentePersonalPatologicoForm(instance=clinical_history.antecedentepersonalpatologico)
    historial_psiquiatrico_quirurgico_form = HistorialPsiquiatricoQuirurgicoForm(instance=clinical_history.historialpsiquiatricoquirurgico)
    antecedente_ginetico_obsetrico_form = AntecedenteGineticoObsetricoForm(instance=clinical_history.antecedentegineticoobsetrico)
    tratamiento_form = TratamientoForm(instance=clinical_history.tratamiento)
    efecto_farmaco_nutricion_form = EfectoFarmacoNutricionForm(instance=clinical_history.efectofarmaconutricion)
    antecedente_personal_no_patologico_form = AntecedentePersonalNoPatologicoForm(instance=clinical_history.antecedentepersonalnopatologico)
    sintomas_actuales_form = SintomasActualesForm(instance=clinical_history.sintomasactuales)
    antecedentes_clinico_anormales_form = AntecedentesClinicoAnormalesForm(instance=clinical_history.antecedentesclinicoanormales)
    antecedentes_problemas_nutricion_form = AntecedentesProblemasNutricionForm(instance=clinical_history.antecedentesproblemasnutricion)
    actividad_fisica_form = ActividadFisicaForm(instance=clinical_history.actividadfisica)
    crono_habitos_form = CronoHabitosForm(instance=clinical_history.cronohabitos)
    indicadores_dieteticos_form = IndicadoresDieteticosForm(instance=clinical_history.indicadoresdieteticos)
    recordatorio_24_hrs_form = Recordatorio24HorasForm(instance=clinical_history.recordatorio24horas)
    frecuencia_alimentos_form = FrecuenciaAlimentosForm(instance=clinical_history.frecuenciaalimentos)
    motivacion_form = MotivacionForm(instance=clinical_history.motivacion)
    metas_form = MetasForm(instance=clinical_history.metas)

    context = {'form': clinical_history_form, 
                'form2': antecedente_familiar_patologico_form,
                'form3': antecedente_personal_patologico_form,
                'form4': historial_psiquiatrico_quirurgico_form,
                'form5': antecedente_ginetico_obsetrico_form,
                'form6': tratamiento_form,
                'form7': efecto_farmaco_nutricion_form,
                'form8': antecedente_personal_no_patologico_form,
                'form9': sintomas_actuales_form,
                'form10': antecedentes_clinico_anormales_form,
                'form11': antecedentes_problemas_nutricion_form,
                'form12': actividad_fisica_form,
                'form13': crono_habitos_form,
                'form14': indicadores_dieteticos_form,
                'form15': recordatorio_24_hrs_form,
                'form16': frecuencia_alimentos_form,
                'form17': motivacion_form,
                'form18': metas_form}

    return render(request, 'view_forms/clinical_history_format_view.html', context)

def render_pdf(template_src):
    template = get_template(template_src)
    html  = template.render()
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def get_clinical_history_pdf_view(request):
    pdf = render_pdf('view_forms/clinical_history_format_view.html')
    return HttpResponse(pdf, content_type='application/pdf')