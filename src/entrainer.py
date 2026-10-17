import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier

params = yaml.safe_load(open('params.yaml', encoding='utf-8'))['entrainement']

train = pd.read_csv('data/prepare/train.csv')
X_train = train.drop(columns=['fraude'])
y_train = train['fraude']

model = RandomForestClassifier(
    n_estimators=params['n_estimators'],
    max_depth=params['max_depth'],
    random_state=params['random_state']
)
model.fit(X_train, y_train)

joblib.dump(model, 'models/model.pkl')
print('Modele entraine et sauvegarde dans models/model.pkl')