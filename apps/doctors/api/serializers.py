from django.db import transaction
from rest_framework import serializers

from apps.doctors.models import DoctorAdmission, Doctor


class GetDoctorTicketSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField()

    def validate_patient_id(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError({"error": "patient_id must be an integer."})
        return value

    def create(self, validated_data):
        doctor_id = 1
        try:
            doctor = Doctor.objects.get(pk=doctor_id)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError({"error": "Doctor is not available."})

        patient_id = validated_data.get("patient_id")
        with transaction.atomic():
            # Check if an admission with this patient_id already exists for the doctor
            if DoctorAdmission.objects.filter(doctor=doctor, patient_id=patient_id).exists():
                raise serializers.ValidationError({"error": "You already reserved for this doctor."})

            current_admissions_count = DoctorAdmission.objects.filter(doctor=doctor).count()

            if current_admissions_count < doctor.admission_count:
                admission = DoctorAdmission.objects.create(
                    doctor=doctor,
                    patient_id=patient_id
                )
                return admission
            else:
                raise serializers.ValidationError({"error": "doctor has no remaining admissions."})
