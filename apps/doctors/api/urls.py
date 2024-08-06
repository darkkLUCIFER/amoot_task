from django.urls import path

from apps.doctors.api import views

app_name = 'doctors'

urlpatterns = [
    path('get-ticket/', views.GetDoctorTicket.as_view(), name='get-ticket'),
]
