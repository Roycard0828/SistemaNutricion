from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AppointmentForm, PrescriptionForm
from .models import Appointment
from patients.models import Patient

# Create your views here.
def create_appointment(request, pk):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            patient = Patient.objects.get(pk=pk)            
            formulario = form.save(commit=False)
            formulario.patient = patient
            formulario.save()
            url = '/patients/patient/{}'.format(pk)
            return redirect(url)
        else:
            return HttpResponse(status=404)

    context = {'form':form}
    return render(request, 'appointments/appointment_form.html', context)

def update_appointment(request, pk):
    
    try:
        appointment = Appointment.objects.get(pk=pk)
        form = AppointmentForm(instance=appointment)
        if request.method == 'POST':
            form = AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                form.save()
                return redirect('get_appointments')                
    except:
        return HttpResponse(status=404)
    
    context = {'form':form}
    return render(request, 'appointments/appointment_form.html', context)

def get_appointments_enabled(request):
     
    appointments = Appointment.objects.filter(finished=False, canceled=False).order_by('fecha')
    context = {'appointments': appointments}
    return render(request, 'appointments/appointments.html', context)

def get_appointment(request, pk):
    try:        
        appointment = Appointment.objects.get(pk=pk)
        form = AppointmentForm(instance=appointment)              
    except:
        return HttpResponse(status=404)
    
    context = {'form':form}
    return render(request, 'appointments/appointment.html', context)