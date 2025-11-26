# Dashboard Température & Humidité - Streamlit

## Description
Ce projet est un dashboard interactif qui affiche en temps réel des données de température et d’humidité. Les données peuvent provenir d’un fichier CSV ou JSON généré par un simulateur (`simulate_writer.py` ou `simulate_writer_json.py`). Le dashboard permet également d’exporter les données affichées.

## Fonctionnalités
- Affichage graphique en direct de la température ou de l’humidité.
- Tableau des 10 dernières mesures.
- Sélecteur de capteur (`Température` / `Humidité`).
- Choix du format d’export (`CSV` ou `JSON`).
- Choix du format de données à lire (`CSV` ou `JSON`).
- Export des données via un bouton.

## Fichiers principaux
- `src/main.py` : Dashboard Streamlit.
- `simulate_writer.py` : Génère des données CSV simulées en continu.
- `simulate_writer_json.py` : Génère des données JSON simulées en continu.
- `data/sample.csv` et `data/sample.json` : fichiers de données générés.
- `exports/` : dossier où sont sauvegardés les fichiers exportés.

## Installation et lancement
1. Créer et activer un environnement virtuel Python.
2. Installer les dépendances :

pip install streamlit pandas numpy

Lancer le simulateur (dans un terminal séparé) :

python src/simulate_writer.py
# ou pour JSON
python src/simulate_writer_json.py


Lancer le dashboard Streamlit (dans un autre terminal) :

streamlit run src/main.py


Ouvrir le navigateur à l’URL indiquée (généralement http://localhost:8501).

---------------------------
┌──────────────────────────┐
│ simulate_writer_json.py  │
│                          │
│ - Génère des données     │
│   toutes les secondes    │
│ - Température / Humidité │
│ - Écrit dans sample.json │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      sample.json         │
│                          │
│ Contient toutes les      │
│ mesures en temps réel    │
│ sous forme de tableau    │
│ [{"timestamp":..., ...}] │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│       main.py            │
│ (Streamlit Dashboard)    │
│                          │
│ - Lit sample.json        │
│ - Affiche graphique      │
│   en fonction du capteur │
│ - Affiche tableau        │
│   des dernières valeurs  │
│ - Export CSV ou JSON     │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│       Navigateur         │
│                          │
│ - Graphiques live        │
│ - Tableau des 10 dernières│
│   mesures                │
│ - Bouton export          │
└──────────────────────────┘

1 Le simulateur tourne dans un terminal et alimente le fichier JSON toutes les secondes.
2 Streamlit lit ce fichier à chaque boucle et met à jour graphique + tableau en direct.
3 Le navigateur montre les changements live et permet d’exporter les données.

## Dashboard Température & Humidité - Guide d'utilisation

### 1. Pré-requis
- Python 3.9+ et Streamlit installé
- Packages Python : `pandas`, `numpy`, `streamlit`
- Deux terminaux disponibles pour lancer le simulateur et le dashboard

### 2. Lancer le simulateur (Terminal 1)
Le simulateur `simulate_writer_json.py` génère des données de température et d'humidité toutes les secondes et les écrit dans `data/sample.json`.  
Commande à exécuter :
```bash
python src/simulate_writer_json.py
3. Lancer le dashboard (Terminal 2)
Le dashboard Streamlit main.py lit le fichier JSON (ou CSV si sélectionné) et met à jour les graphiques et le tableau en temps réel.
Commande à exécuter :


streamlit run src/main.py

Flux de données

Le simulateur écrit dans data/sample.json toutes les secondes.
Streamlit lit ce fichier à chaque boucle et met à jour :
le graphique en fonction du capteur sélectionné (Température ou Humidité)
le tableau des 10 dernières mesures
L’utilisateur peut exporter les données via le bouton Export (CSV ou JSON).

Navigation et captures d’écran

Pour documenter le projet, prendre des screenshots à chaque étape :
screenshot_launch_streamlit.png → écran de lancement (terminal + navigateur)
screenshot_dashboard_initial.png → page principale / état initial du dashboard
screenshot_dashboard_live.png → page en « live » (graphes mis à jour)
screenshot_export_files.png → action d’export (bouton Export ou fichier ouvert)
screenshot_filter_X.png → exemple d’utilisation d’un filtre (ex : sélection d’un capteur)

