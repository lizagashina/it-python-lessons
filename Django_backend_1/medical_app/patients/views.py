# patients/views.py
from django.shortcuts import render, redirect
from .models import Patient, HealthRecord


def register_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Получаем значение поля 'name' из POST-запроса
        age = int(request.POST.get('age'))  # Получаем значение поля 'age' из POST-запроса и преобразуем его в целое число
        gender = request.POST.get('gender')  # Получаем значение поля 'gender' из POST-запроса
        patient = Patient.objects.create(name=name, age=age, gender=gender)  # Создаем новый объект Patient с указанными значениями
        return redirect('health_record', patient_id=patient.id)  # Перенаправляем пользователя на страницу 'health_record' с идентификатором созданного пациента

    return render(request, 'register_patient.html')  # Отображаем шаблон 'register_patient.html'


def health_record(request, patient_id):
    patient = Patient.objects.get(id=patient_id)  # Получаем объект Patient по указанному идентификатору
    if request.method == 'POST':
        blood_pressure = request.POST.get('blood_pressure')  # Получаем значение поля 'blood_pressure' из POST-запроса
        pulse = int(request.POST.get('pulse'))  # Получаем значение поля 'pulse' из POST-запроса и преобразуем его в целое число
        temperature = float(request.POST.get('temperature'))  # Получаем значение поля 'temperature' из POST-запроса и преобразуем его в число с плавающей запятой
        HealthRecord.objects.create(patient=patient, blood_pressure=blood_pressure, pulse=pulse,
                                    temperature=temperature)  # Создаем новую запись HealthRecord с указанными значениями

    records = HealthRecord.objects.filter(patient=patient)  # Получаем все записи HealthRecord, связанные с указанным пациентом
    context = {'patient': patient, 'records': records}  # Создаем контекст для передачи данных в шаблон
    return render(request, 'health_record.html', context)  # Отображаем шаблон 'health_record.html' с переданным контекстом