# mlops-tp6-workflows

Copie du depot [mlops-tp3-dvc](https://github.com/aymanesalkhi1/mlops-tp3-dvc), etendue pour le TP06 (5IASD, Deploiement d'IA) : le pipeline DVC de detection de fraude devient un workflow Prefect, avec une regle de qualite et une verification GitHub Actions.

Le jeu v2 (graines fixes des scripts du cours) donne **F1 = 0.8423**, au-dessus du seuil **0.82**. Avec `max_depth: 2`, le F1 tombe a **0.25** et le workflow s'arrete.

## Lancer en local

```bash
cd tp6-workflows
python -m venv .venv
# Windows : .venv\Scripts\Activate.ps1
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Si le stockage DVC local n'est pas la :
python donnees.py
python nouvelles_donnees.py
dvc repro

# Terminal 1
prefect server start

# Terminal 2
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
python flow_mlops.py
python verifier_qualite.py

# Terminal 3 : planification (laisser ouvert)
python planifier.py

# Ou le couple pool / worker
prefect work-pool create pool-tp --type process
prefect deploy --all --no-prompt
prefect worker start --pool pool-tp
```

`prefect.yaml` fixe le dossier de travail du worker. Si le projet est deplace, mettre a jour `pull.directory` avec le chemin absolu du clone, puis relancer `prefect deploy --all`.

Le remote DVC reste `../../dvc-stockage`, a cote de ce dossier, comme au TP3. La CI ne fait pas `dvc pull` : elle rejoue `donnees.py` puis `nouvelles_donnees.py`.
