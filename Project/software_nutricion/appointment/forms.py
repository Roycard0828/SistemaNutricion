from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class AppointmentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for field in self.fields.keys():
                self.fields[field].widget.attrs['readonly'] = True
    
    class Meta:
        model = Appointment
        exclude = ['patient']
        widgets = {
            'fecha': DateInput(),
        }       

class PrescriptionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            for field in self.fields.keys():
                self.fields[field].widget.attrs['readonly'] = True
    
    class Meta:
        model = Prescription
        exclude = ['appointment']  