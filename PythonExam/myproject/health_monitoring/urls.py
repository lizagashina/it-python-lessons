# health_monitoring/urls.py
from django.urls import path
from .views import patient_list, patient_detail

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('health_record/<int:pk>/', patient_detail, name='health_record'),
]