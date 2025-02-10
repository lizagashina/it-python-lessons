import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from health_monitoring.models import Patient, HealthRecord

# Очистка базы перед загрузкой
HealthRecord.objects.all().delete()
Patient.objects.all().delete()

csv_file = "medical_examination.csv"
df = pd.read_csv(csv_file)
GENDER_MAPPING = {1: "Муж", 2: "Жен"}

records_to_create = []

for _, row in df.iterrows():
    gender = GENDER_MAPPING.get(row["gender"], "Неизвестно")

    patient = Patient.objects.create(  # Создаем нового пациента для каждой строки
        age=int(row["age"] / 365),
        gender=gender
    )

    records_to_create.append(
        HealthRecord(
            patient=patient,
            height=row["height"],
            weight=row["weight"],
            systolic_pressure=row["ap_hi"],
            diastolic_pressure=row["ap_lo"],
            smoke=bool(row["smoke"]),
            alco=bool(row["alco"]),
            active=bool(row["active"]),
            cardio=bool(row["cardio"])
        )
    )

HealthRecord.objects.bulk_create(records_to_create)  # Оптимизированная массовая вставка
print("База очищена и данные успешно загружены!")
