from django.contrib import admin

from apps.doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'admission_count']
