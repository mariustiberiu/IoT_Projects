# 03 - Stockage des mesures en SQLite

## 🎯 Objectif
Lire des mesures de température et humidité (simulation ou Arduino), les stocker dans une base SQLite, puis permettre l’export et la visualisation.

## 🛠 Technologies
- Python 3.13
- sqlite3 (intégré à Python)
- pandas (pour export CSV/JSON)
- matplotlib (pour graphiques)
- pyserial (si acquisition réelle depuis Arduino)

## 📂 Structure du projet

- `src/` : scripts Python
  - `acquisition_sqlite.py` → simulation ou acquisition réelle
  - `backup_and_export.py` → backup + export CSV/JSON
  - `export_csv.py` → export CSV (optionnel si séparé)
- `data/` : base SQLite et exports (ignoré par Git)
  - `capteurs.db` → DB principale
  - `sample_small.db` → mini DB pour tests rapides
- `.venv/` : environnement virtuel Python (non versionné)
- `.gitignore` : fichiers ignorés
- `README.md` : documentation

## 📝 Utilisation

1. Créer l’environnement virtuel :

```bash
python -m venv .venv
