from http.client import OK, HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Patient
from .forms import PatientForm
from clinical_history.helpers.path_enumerations import PathEnumerations

# Create your views here.
def create_patient(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patients')
        else:
            return HTTPResponse(status=404)

    context = {'form':form}
    return render(request, 'patients/patient_form.html', context)

def get_patient(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
        has_clinical_history = hasattr(patient, 'clinicalhistory')
        if has_clinical_history:
            step = patient.clinicalhistory.steps
            finished = patient.clinicalhistory.finished
        else:
            step = ''
            finished = ""

        appointments = patient.appointment_set.all()
    except:
        return HttpResponse(status=404)
    
    context = {'patient':patient,'has_clinical_history':has_clinical_history, 'step':step, 'finished':finished, 'appointments': appointments}

    return render(request, 'patients/patient_profile.html', context)

def delete_patient(request, pk):

    try:
        patient = Patient.objects.get(pk=pk)
        context = {'object':patient}

        if request.method == 'POST':                  
            patient.delete()                
            return redirect('patients') # NOTA: redigir al main        
    except:
        context = {'object':None}
        return HttpResponse(status=404)

    return render(request, 'patients/delete_patient.html', context)

def update_patient(request, pk):
        
    try:
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient)

        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)

            if form.is_valid():
                form.save()
                return redirect('patients')
                #return redirect('patient', pk=patient.id)
    except:
        return HttpResponse(status=404)

    context = {'form':form}

    return render(request, 'patients/patient_form.html', context)

def get_all_patients(request):
    patients = Patient.objects.all()
    
    context = {'patients': patients}

    return render(request, 'patients/patients.html', context)


def continue_view(request, pk):
    #Continuar con el historial clinico
    patient = Patient.objects.get(pk=pk)
    clinical_history = patient.clinicalhistory
    step = clinical_history.steps
    enumerations = [x.value for x in list(PathEnumerations)]
    following = enumerations[step]
    url = '/clinical_history/create/{}/{}'.format(following, pk)
    return redirect(url, pk=pk)

