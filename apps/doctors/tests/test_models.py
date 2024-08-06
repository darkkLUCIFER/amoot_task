from django.test import TestCase
from apps.doctors.models import Doctor
from django.contrib.auth import get_user_model

User = get_user_model()


class DoctorModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user_1', password='password')
        self.doctor = Doctor.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            admission_count=10
        )

    def test_doctor_creation(self):
        self.assertIsInstance(self.doctor, Doctor)
        self.assertEqual(self.doctor.user, self.user)
        self.assertEqual(self.doctor.admission_count, 10)

    def test_created_at_and_updated_at(self):
        self.assertIsNotNone(self.doctor.created_at)
        self.assertIsNotNone(self.doctor.updated_at)

    def test_doctor_string_representation(self):
        self.assertEqual(str(self.doctor), 'John Doe')

    def test_admission_count_default(self):
        # Create a new user for this test
        user = User.objects.create_user(username='test_user_2', password='password')
        doctor_without_admission_count = Doctor.objects.create(user=user, first_name='Jane', last_name='Doe')
        self.assertEqual(doctor_without_admission_count.admission_count, 0)
