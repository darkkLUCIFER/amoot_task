from rest_framework import serializers

from apps.doctors.models import DoctorAdmission, Doctor


class GetDoctorTicketSerializer(serializers.Serializer):
    patient_id = serializers.IntegerField()

    def validate_patient_id(self, value):
        doctor_admission = DoctorAdmission.objects.filter(patient_id=value)
        if doctor_admission:
            raise serializers.ValidationError({"error": "you already reserved for this doctor"})
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

        current_admissions_count = DoctorAdmission.objects.filter(doctor=doctor).count()

        if current_admissions_count < doctor.admission_count:
            DoctorAdmission.objects.create(
                doctor=doctor,
                patient_id=patient_id
            )
        else:
            raise serializers.ValidationError({"error": "doctor has no remaining admissions."})
        return validated_data
