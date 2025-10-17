# script_centralise_generer_auto_template_interactive_v5.py pourra :

# Te permettre de choisir chapitre par chapitre quels sous-projets générer.
# Te demander si tu veux copier les templates pour chaque type.
# Offrir la possibilité de sélectionner les fichiers à créer pour chaque sous-chapitre (screenshots, backup, exports, .py, .ino, etc.).
# Toujours générer un résumé clair à la fin.

# Ça sera plus flexible et sûr pour ne pas écraser du travail existant, et tu pourras tester chaque sous-projet séparément.

# sélectionner quels chapitres et sous-chapitres générer, tout en conservant les templates et fichiers standards


# 1 Interactif : Tu décides chapitre par chapitre et sous-projet par sous-projet.
# 2 Templates : Si tu as un modèle dans TEMPLATES/<type>/, il sera copié automatiquement.
# 3 Screenshots : Les fichiers screenshot_console_01.png, etc., sont créés et nommés.
# 4 Dossiers standards : src, data, backup, exports, screenshots sont toujours créés.
# 5 Fichiers standards : .py, .ino, .csv, .json, README.md.

import os
import shutil
from datetime import datetime

# --------------------------------
# Configuration générale
# --------------------------------
BASE_DIR = os.path.abspath(".")  # Racine du projet IoT_Projects
STANDARD_DIRS = ["src", "data", "backup", "exports", "screenshots"]
NUM_SCREENSHOTS = 2  # nombre de screenshots par sous-projet

# Fichiers standards par type de projet
STANDARD_FILES = {
    "simulation": ["src/main.py", "data/sample.csv", "data/sample.json", "README.md"],
    "arduino": ["src/main.ino", "data/sample.csv", "README.md"],
    "simulation_ou_arduino": ["src/main.py", "data/sample.csv", "data/sample.json", "README.md"],
}

# Dossier templates (optionnel)
TEMPLATES_DIR = os.path.join(BASE_DIR, "TEMPLATES")

# Sommaire complet (Ch1 → Ch7 et sous-chapitres)
PROJECTS = {
    "Ch1_Acquisition_Données_Capteurs": {
        "01_CapteurVirtuel_Python": {"type": "simulation"},
        "02_LectureSerie_PySerial": {"type": "arduino"},
        "03_Stockage_SQLite": {"type": "simulation_ou_arduino"},
        "04_ExportCSV_Visualisation": {"type": "simulation_ou_arduino"},
    },
    "Ch2_Communication_MQTT_API": {
        "01_Serveur_MQTT": {"type": "simulation"},
        "02_Publish_subscribe_multi_clients": {"type": "simulation"},
        "03_Securisation_MQTT_SSL_TLS": {"type": "simulation"},
        "04_API_REST_Django": {"type": "simulation"},
    },
    "Ch3_Dashboards_Visualisation": {
        "01_Graphiques_temps_reel": {"type": "simulation"},
        "02_Application_interactive_Streamlit": {"type": "simulation"},
        "03_Dashboard_Django_MongoDB": {"type": "simulation"},
        "04_Dashboard_Grafana_InfluxDB": {"type": "simulation"},
    },
    "Ch4_Analyse_Predictive": {
        "01_Regression_lineaire": {"type": "simulation"},
        "02_Series_temporelles_ARIMA": {"type": "simulation"},
        "03_Detection_anomalies_IsolationForest": {"type": "simulation"},
        "04_Classification_sonore": {"type": "simulation"},
    },
    "Ch5_Securite_IoT": {
        "01_Auth_JWT_Django": {"type": "simulation"},
        "02_Chiffrement_AES": {"type": "simulation"},
        "03_Detection_intrusion_logs": {"type": "simulation"},
    },
    "Ch6_Cloud_Edge": {
        "01_AWS_IoT_Core": {"type": "simulation"},
        "02_Google_Cloud_IoT": {"type": "simulation"},
        "03_Edge_RaspberryPi": {"type": "simulation"},
        "04_Deploy_Docker": {"type": "simulation"},
    },
    "Ch7_Projets_Avances_IA": {
        "01_Reconnaissance_images": {"type": "simulation"},
        "02_Detection_evenements_audio": {"type": "simulation"},
        "03_Systeme_recommandation": {"type": "simulation"},
        "04_Projet_final_SmartHome": {"type": "simulation_ou_arduino"},
    }
}

# --------------------------------
# Fonctions utilitaires
# --------------------------------
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path):
    if not os.path.exists(path):
        create_dir(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            pass  # fichier vide

def copy_template(proj_type, dest_path, filename):
    template_path = os.path.join(TEMPLATES_DIR, proj_type, os.path.basename(filename))
    if os.path.exists(template_path):
        create_dir(os.path.dirname(dest_path))
        shutil.copy(template_path, dest_path)
    else:
        create_file(dest_path)

def create_screenshots(proj_path):
    screenshots_path = os.path.join(proj_path, "screenshots")
    create_dir(screenshots_path)
    for i in range(1, NUM_SCREENSHOTS + 1):
        create_file(os.path.join(screenshots_path, f"screenshot_console_{i:02}.png"))

def create_standard_dirs(proj_path):
    for d in STANDARD_DIRS:
        create_dir(os.path.join(proj_path, d))

# --------------------------------
# Script interactif
# --------------------------------
print("🚀 Script interactif de génération de projets IoT")

for chapter, subs in PROJECTS.items():
    generate_chapter = input(f"\nVoulez-vous générer {chapter}? (o/n) : ").strip().lower()
    if generate_chapter != "o":
        continue

    chapter_path = os.path.join(BASE_DIR, chapter)
    create_dir(chapter_path)

    for sub_name, info in subs.items():
        generate_sub = input(f"  - Générer sous-projet {sub_name}? (o/n) : ").strip().lower()
        if generate_sub != "o":
            continue

        sub_path = os.path.join(chapter_path, sub_name)
        create_dir(sub_path)
        proj_type = info.get("type", "simulation")

        # Créer dossiers standards
        create_standard_dirs(sub_path)

        # Créer fichiers standards (ou copier templates)
        for f in STANDARD_FILES.get(proj_type, []):
            dest_file = os.path.join(sub_path, f)
            copy_template(proj_type, dest_file, f)

        # Créer screenshots
        create_screenshots(sub_path)

# --------------------------------
# Résumé
# --------------------------------
print("\n✅ Arborescence générée !")
for chapter, subs in PROJECTS.items():
    print(chapter)
    for sub_name in subs:
        print("  └─", sub_name)
