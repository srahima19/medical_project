import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

data = {
    'fever':               [1,0,1,0,1,1,0,1,0,1,0,1],
    'cough':               [1,1,0,0,1,0,1,0,1,1,1,0],
    'headache':            [0,1,1,0,0,1,1,1,0,0,1,1],
    'fatigue':             [1,0,0,1,1,1,0,0,1,1,0,1],
    'nausea':              [0,0,1,1,0,0,1,0,1,0,1,0],
    'chest_pain':          [0,0,0,0,0,0,0,1,0,0,0,1],
    'shortness_of_breath': [0,0,0,0,0,0,0,1,0,0,0,1],
    'sore_throat':         [1,1,0,0,1,0,1,0,0,1,0,0],
    'disease': [
        'Flu','Cold','Migraine','Anemia','Flu',
        'Flu','Cold','Heart Issue','Anemia','Flu',
        'Cold','Heart Issue'
    ]
}

df = pd.DataFrame(data)
X = df.drop('disease', axis=1)
y = df['disease']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

save_dir = os.path.join(os.path.dirname(__file__), 'ml_model')
os.makedirs(save_dir, exist_ok=True)

joblib.dump(model, os.path.join(save_dir, 'model.pkl'))
joblib.dump(list(X.columns), os.path.join(save_dir, 'features.pkl'))

print("Model trained and saved successfully!")
print(f"Saved to: {save_dir}")