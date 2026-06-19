from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Patient

SYMPTOM_CHOICES = [
    ('fever', 'Fever'),
    ('cough', 'Cough'),
    ('headache', 'Headache'),
    ('fatigue', 'Fatigue'),
    ('nausea', 'Nausea'),
    ('chest_pain', 'Chest Pain'),
    ('shortness_of_breath', 'Shortness of Breath'),
    ('sore_throat', 'Sore Throat'),
]

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField(min_value=1, max_value=120)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'password1', 'password2', 'age', 'gender']

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=SYMPTOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Select your symptoms'
    )