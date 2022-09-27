from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import create_patient, delete_patient, update_patient, get_all_patients, get_patient

class TestUrls(SimpleTestCase):

    def test_create_patients_urls_works(self):
        url = reverse('create_patient')
        self.assertEquals(resolve(url).func, create_patient)
    
    def test_delete_patients_urls_works(self):
        url = reverse('delete_patient', args=[1])
        self.assertEquals(resolve(url).func, delete_patient)
    
    def test_get_patient_url_works(self):
        url = reverse('get_patient', args=[1])
        self.assertEquals(resolve(url).func, get_patient)
    
    def test_update_patients_urls_works(self):
        url = reverse('update_patient', args=[1])
        self.assertEquals(resolve(url).func, update_patient)

    def test_get_all_patients_urls_works(self):
        url = reverse('patients')
        self.assertEquals(resolve(url).func, get_all_patients)

