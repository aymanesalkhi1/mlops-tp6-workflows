import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 5000

montant = np.round(rng.lognormal(6.0, 1.2, n), 2)
anciennete = rng.integers(0, 120, n)
freq = rng.poisson(3, n) + 1
nuit = rng.binomial(1, 0.15, n)

score = 2.0 * (np.log10(montant) - 3.0) - anciennete / 60 + (freq - 3) / 3 + nuit * 1.5
fraude = ((score + rng.normal(0, 0.4, n)) > 0.5).astype(int)

df = pd.DataFrame({
    'montant': montant,
    'anciennete': anciennete,
    'freq_24h': freq,
    'nuit': nuit,
    'fraude': fraude
})

df.to_csv('data/transactions.csv', index=False)
print('data/transactions.csv ecrit:', len(df), 'lignes,', df['fraude'].sum(), 'fraudes')