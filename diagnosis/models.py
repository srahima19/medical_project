from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptoms = models.TextField()
    predicted_disease = models.CharField(max_length=200)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} - {self.predicted_disease}"