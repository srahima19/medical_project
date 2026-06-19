# medical_project
AI Medical Diagnosis Assistant using Django
# AI-Powered Medical Diagnosis Assistant
A Django web application that uses Machine Learning to predict possible
diseases based on patient symptoms.

## Features
- User registration and login system
- Symptom selection form
- AI-based disease prediction using Random Forest
- Diagnosis history dashboard
- Django admin panel

## Tech Stack
- Python 3.12
- Django 5.x
- scikit-learn
- pandas, numpy, joblib
- Bootstrap 5

## Installation & Setup

### 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/medical_project.git
cd medical_project

### 2. Install dependencies
pip install -r requirements.txt

### 3. Train the ML model
python diagnosis/train_model.py

### 4. Run migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create admin user
python manage.py createsuperuser

### 6. Run the server
python manage.py runserver

Then open http://127.0.0.1:8000 in your browser.

## Project Structure
medical_project/
├── manage.py
├── requirements.txt
├── medical_project/
│   ├── settings.py
│   └── urls.py
└── diagnosis/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── train_model.py
    ├── admin.py
    ├── ml_model/
    └── templates/

## Disclaimer
This system does not replace professional medical advice.
It only provides predictive assistance based on machine learning models.
