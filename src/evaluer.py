import json
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, f1_score, precision_score, recall_score

test = pd.read_csv('data/prepare/test.csv')
X_test = test.drop(columns=['fraude'])
y_test = test['fraude']

model = joblib.load('models/model.pkl')
y_pred = model.predict(X_test)

metrics = {
    'accuracy': round(float(accuracy_score(y_test, y_pred)), 4),
    'precision': round(float(precision_score(y_test, y_pred)), 4),
    'recall': round(float(recall_score(y_test, y_pred)), 4),
    'f1': round(float(f1_score(y_test, y_pred)), 4)
}

with open('reports/metrics.json', 'w', encoding='utf-8') as f:
    json.dump(metrics, f, indent=2)

fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax)
plt.savefig('reports/confusion.png')

print('Evaluation terminee. Metrics:', metrics)