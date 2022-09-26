from http.client import OK, HTTPResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Patient

from .forms import PatientForm

# Create your views here.
def create_patient(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patients')

    context = {'form':form}
    return render(request, 'patients/patient_form.html', context)

def get_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {'patient':patient}
    return render(request, 'patients/patient_profile.html', context)

def delete_patient(request, pk):

    try:
        patient = Patient.objects.get(pk=pk)

        if request.method == 'POST':                  
            patient.delete()                
            return redirect('patients') # NOTA: redigir al main

        context = {'object':patient}
    except:
        context = {'object':None}

    return render(request, 'patients/delete_patient.html', context)


def update_patients(request, pk):
        
    try:
        patient = Patient.objects.get(pk=pk)
        form = PatientForm(instance=patient)

        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)

            if form.is_valid():
                form.save()
                return redirect('patients')
    except:
        return HTTPResponse('Patient not found')

    context = {'form':form}

    return render(request, 'patients/patient_form.html', context)

def get_all_patients(request):
    patients = Patient.objects.all()
    
    context = {'patients': patients}

    return render(request, 'patients/patients.html', context)