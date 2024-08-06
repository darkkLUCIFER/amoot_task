from django.contrib import admin

from apps.doctors.models import Doctor, DoctorAdmission


class DoctorAdmissionInline(admin.TabularInline):
    model = DoctorAdmission
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False




@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'admission_count']
    inlines = [DoctorAdmissionInline]
