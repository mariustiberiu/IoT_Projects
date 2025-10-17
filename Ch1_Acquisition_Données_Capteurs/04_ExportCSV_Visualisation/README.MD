# Chapitre 4 : Export & Visualisation CSV/JSON

Ce chapitre présente un petit projet d’exportation de données depuis une base SQLite et de visualisation avec Python. Les exports peuvent être au format CSV ou JSON, et un affichage graphique interactif est disponible pour les données numériques.

---

## Structure du projet
04_ExportCSV_Visualisation/
├─ data/ # Base de données SQLite et fichiers de démonstration
│ ├─ capteurs.db
│ ├─ sample.csv
│ └─ sample.json
├─ exports/ # Dossier où sont générés les exports CSV/JSON
│ ├─ data.csv
│ └─ export_data.json
├─ screenshots/ # Captures d’écran pour GitHub/CV
├─ src/
│ ├─ export_csv.py # Fonction principale d’export CSV/JSON
│ ├─ main.py # Script interactif pour exporter et visualiser les données
│ └─ init.py
├─ requirements.txt # Librairies Python nécessaires (pandas, matplotlib, etc.)
└─ README.md


---

## Installation

1. Cloner le projet :

```bash
git clone <URL_DU_PROJET>
cd 04_ExportCSV_Visualisation

Créer un environnement virtuel et installer les dépendances :
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows PowerShell
pip install -r requirements.txt

1. Export CSV ou JSON depuis la base SQLite
# Export CSV
python src/export_csv.py --db data/capteurs.db --format csv --output exports/data.csv

# Export JSON
python src/export_csv.py --db data/capteurs.db --format json --output exports/data.json

2. Export avec données simulées
# Export CSV simulé
python src/export_csv.py --format csv --output exports/data.csv --simulate

# Export JSON simulé
python src/export_csv.py --format json --output exports/data.json --simulate

3. Script interactif de visualisation
python src/main.py

Il vous demande si vous souhaitez utiliser des données simulées.

Après l’export, vous pouvez choisir d’afficher un graphique interactif des données CSV/JSON.


---

