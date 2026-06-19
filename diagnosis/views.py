from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, SymptomForm
from .models import Patient, Diagnosis
import joblib
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'model.pkl')
FEATURES_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'features.pkl')

def load_model():
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        features = joblib.load(FEATURES_PATH)
        return model, features
    return None, None

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Patient.objects.create(
                user=user,
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender']
            )
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'diagnosis/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'diagnosis/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    try:
        patient = request.user.patient
        history = Diagnosis.objects.filter(patient=patient).order_by('-created_at')
    except Patient.DoesNotExist:
        history = []
    return render(request, 'diagnosis/dashboard.html', {'history': history})

@login_required
def predict_view(request):
    model, features = load_model()
    if model is None:
        return render(request, 'diagnosis/predict.html', {
            'form': SymptomForm(),
            'error': 'ML model not found. Please run train_model.py first.'
        })

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            selected = form.cleaned_data['symptoms']
            input_vec = [1 if f in selected else 0 for f in features]
            input_arr = np.array(input_vec).reshape(1, -1)

            prediction = model.predict(input_arr)[0]
            proba = model.predict_proba(input_arr).max()

            try:
                patient = request.user.patient
            except Patient.DoesNotExist:
                patient = Patient.objects.create(
                    user=request.user, age=0, gender='Unknown'
                )

            diag = Diagnosis.objects.create(
                patient=patient,
                symptoms=', '.join(selected),
                predicted_disease=prediction,
                confidence=round(proba * 100, 2)
            )
            return redirect('result', pk=diag.pk)
    else:
        form = SymptomForm()
    return render(request, 'diagnosis/predict.html', {'form': form})

@login_required
def result_view(request, pk):
    diag = get_object_or_404(Diagnosis, pk=pk)
    return render(request, 'diagnosis/result.html', {'diag': diag})