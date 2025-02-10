# patients/models.py
from django.db import models

class Patient(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.FloatField()
    systolic_pressure = models.IntegerField()
    diastolic_pressure = models.IntegerField()
    smoke = models.BooleanField()
    alco = models.BooleanField()
    active = models.BooleanField()
    cardio = models.BooleanField()