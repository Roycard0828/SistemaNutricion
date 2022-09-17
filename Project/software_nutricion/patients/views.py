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
            return redirect('get_patient', patient.id)

    context = {'form':form}
    return render(request, 'patients/create_patient.html', context)

def get_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {'patient':patient}
    return render(request, 'patients/patient_profile.html', context)
