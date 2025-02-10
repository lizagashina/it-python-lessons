from django.shortcuts import render, get_object_or_404
from .models import Patient, HealthRecord

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    health_record = HealthRecord.objects.filter(patient=patient).first()
    return render(request, 'patient_detail.html', {'patient': patient, 'health_record': health_record})
