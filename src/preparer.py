import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open('params.yaml', encoding='utf-8'))['preparation']

df = pd.read_csv('data/transactions.csv')

train, test = train_test_split(
    df,
    test_size=params['test_size'],
    random_state=params['random_state'],
    stratify=df['fraude']
)

train.to_csv('data/prepare/train.csv', index=False)
test.to_csv('data/prepare/test.csv', index=False)
print('Pre-traitement termine: train', len(train), 'lignes, test', len(test), 'lignes')