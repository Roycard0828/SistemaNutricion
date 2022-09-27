from django.test import TestCase, Client
from django.urls import reverse 

from ..views import create_patient, delete_patient, update_patient, get_patient, get_all_patients
from ..models import Patient

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_patient_view(self):    
        url = reverse('create_patient')
        response = self.client.post(url, {
            'nombre' : 'Rodrigo',
            'apellidos' : 'Garcia',
            'edad' : 21,
            'direccion' : 'Av 12',
            'telefono' : '22222',
            'ocupacion' : 'estudiante'
        })

        self.assertEquals(response.status_code, 302)
    
    def test_delete_patients_works(self):
        patient = Patient.objects.create(
            nombre = 'Rodrigo',
            apellidos = 'Garcia',
            edad = 21,
            direccion = 'Av 12',
            telefono = '22222',
            ocupacion = 'estudiante'
        )
        url = reverse('delete_patient', args=[patient.id])
        response = self.client.post(url)
        self.assertEquals(response.status_code, 302)
    
    def test_delete_patients_not_found_patient(self):
        url = reverse('delete_patient', args=[1])
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

    def test_update_patients_works(self):
        patient = Patient.objects.create(
            nombre = 'Rodrigo',
            apellidos = 'Garcia',
            edad = 21,
            direccion = 'Av 12',
            telefono = '22222',
            ocupacion = 'estudiante'
        )
        url = reverse('update_patient', args=[patient.id])
        response = self.client.post(url, {
            'nombre' : 'Rodrigo',
            'apellidos' : 'Garcia',
            'edad' : 21,
            'direccion' : 'Av 12',
            'telefono' : '22222',
            'ocupacion': 'Desarrollador',
        })
        self.assertEquals(response.status_code, 302)

    def test_update_patients_not_found(self):
        url = reverse('update_patient', args=[1])
        response = self.client.post(url)
        self.assertEquals(response.status_code, 404)

    def test_get_all_patients_works(self):
        url = reverse('patients')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_get_patient_works(self):
        patient = Patient.objects.create(
            nombre = 'Rodrigo',
            apellidos = 'Garcia',
            edad = 21,
            direccion = 'Av 12',
            telefono = '22222',
            ocupacion = 'estudiante'
        )
        url = reverse('get_patient', args=[patient.id])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)