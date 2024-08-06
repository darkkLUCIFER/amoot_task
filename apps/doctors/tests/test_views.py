from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.doctors.models import Doctor, DoctorAdmission

User = get_user_model()


class GetDoctorTicketAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user_1', password='password')
        self.doctor = Doctor.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            admission_count=10
        )
        self.url = reverse('doctors:create-ticket')

    def test_create_doctor_ticket(self):
        data = {'patient_id': 1}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DoctorAdmission.objects.count(), 1)
        self.assertEqual(DoctorAdmission.objects.first().patient_id, 1)

    def test_create_doctor_ticket_limit_reached(self):
        # Create enough admissions to reach the limit
        for _ in range(self.doctor.admission_count):
            DoctorAdmission.objects.create(doctor=self.doctor, patient_id=_ + 1)

        data = {'patient_id': 11}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'],
                         'doctor has no remaining admissions.')
