# script_centralise_generer_auto_v3.py, prête à exécuter. 
# Elle crée tous les chapitres Ch1 → Ch7, tous les sous-chapitres, 
# les dossiers standards, les fichiers (même vides), 
# les screenshots nommés correctement et les fichiers backup/exports 
# avec timestamp.


# ✅ Ce script fait tout automatiquement :

# Crée tous les dossiers src, data, backup, exports, screenshots.

# Crée tous les fichiers standards vides ou avec extension .py, .ino, .csv, .json, .md.

# Génère screenshot_console_01.png, screenshot_console_02.png pour chaque sous-chapitre.

# Crée backup et exports avec un fichier timestamp.

# Respecte exactement tes noms de chapitres et sous-chapitres.

import os
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

# --------------------------------
# Sommaire complet (Ch1 → Ch7)
# --------------------------------
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
    },
}

# --------------------------------
# Fonctions utilitaires
# --------------------------------
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path):
    create_dir(os.path.dirname(path))
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass  # fichier vide

def create_screenshots(proj_path):
    screenshots_dir = os.path.join(proj_path, "screenshots")
    create_dir(screenshots_dir)
    for i in range(1, NUM_SCREENSHOTS + 1):
        file_path = os.path.join(screenshots_dir, f"screenshot_console_{i:02}.png")
        create_file(file_path)

def create_backup_exports(proj_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for folder in ["backup", "exports"]:
        dir_path = os.path.join(proj_path, folder)
        create_dir(dir_path)
        # créer un fichier vide avec timestamp comme exemple
        create_file(os.path.join(dir_path, f"{folder}_{timestamp}.txt"))

# --------------------------------
# Création de l’arborescence complète
# --------------------------------
for chapter, subprojects in PROJECTS.items():
    chapter_path = os.path.join(BASE_DIR, chapter)
    create_dir(chapter_path)
    for sub_name, info in subprojects.items():
        sub_path = os.path.join(chapter_path, sub_name)
        create_dir(sub_path)

        # Créer tous les dossiers standards
        for d in STANDARD_DIRS:
            create_dir(os.path.join(sub_path, d))

        # Créer les fichiers standards selon type
        proj_type = info.get("type", "simulation")
        for f in STANDARD_FILES.get(proj_type, []):
            file_path = os.path.join(sub_path, f)
            create_file(file_path)

        # Créer screenshots
        create_screenshots(sub_path)

        # Créer backup et exports
        create_backup_exports(sub_path)

# --------------------------------
# Résumé
# --------------------------------
print("✅ Arborescence complète générée pour tous les chapitres et sous-projets.")
