from django.urls import path

from apps.doctors.api import views

app_name = 'doctors'

urlpatterns = [
    path('create-ticket/', views.CreateDoctorTicketView.as_view(), name='create-ticket'),
]
