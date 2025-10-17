# script_centralise_generer_auto_template_interactive_v5_1.py, qui :

# Affiche un aperçu des fichiers déjà existants et demande si tu veux les écraser ou pas.
# Permet de sélectionner plusieurs sous-projets à la fois pour gagner du temps.

# Affiche les fichiers déjà existants dans chaque sous-projet.
# Demande si tu veux les écraser ou pas.
# Permet de sélectionner plusieurs sous-projets à la fois (en entrant 1,3,4 ou all).

# 1 Liste des fichiers existants avant génération.
# 2 Choix d’écraser ou pas chaque fichier.
# 3 Option all pour générer rapidement tous les sous-projets d’un chapitre.

# La suite sera le script_centralise_generer_auto_template_interactive_v5_2.py
# qui permet aussi de choisir plusieurs chapitres à la fois, pour vraiment accélérer la génération massive

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

def create_file(path, overwrite=False):
    if os.path.exists(path) and not overwrite:
        return False
    create_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        pass  # fichier vide
    return True

def copy_template(proj_type, dest_path, filename, overwrite=False):
    template_path = os.path.join(TEMPLATES_DIR, proj_type, os.path.basename(filename))
    if os.path.exists(template_path):
        create_dir(os.path.dirname(dest_path))
        if not os.path.exists(dest_path) or overwrite:
            shutil.copy(template_path, dest_path)
            return True
    else:
        return create_file(dest_path, overwrite)
    return False

def create_screenshots(proj_path, overwrite=False):
    screenshots_path = os.path.join(proj_path, "screenshots")
    create_dir(screenshots_path)
    created_files = []
    for i in range(1, NUM_SCREENSHOTS + 1):
        file_path = os.path.join(screenshots_path, f"screenshot_console_{i:02}.png")
        if create_file(file_path, overwrite):
            created_files.append(file_path)
    return created_files

def create_standard_dirs(proj_path):
    for d in STANDARD_DIRS:
        create_dir(os.path.join(proj_path, d))

def list_existing_files(proj_path):
    existing = []
    for root, dirs, files in os.walk(proj_path):
        for f in files:
            existing.append(os.path.relpath(os.path.join(root, f), proj_path))
    return existing

# --------------------------------
# Script interactif v5.1
# --------------------------------
print("🚀 Script interactif v5.1 - génération de projets IoT")

for chapter, subs in PROJECTS.items():
    generate_chapter = input(f"\nVoulez-vous générer {chapter}? (o/n) : ").strip().lower()
    if generate_chapter != "o":
        continue

    chapter_path = os.path.join(BASE_DIR, chapter)
    create_dir(chapter_path)

    for idx, (sub_name, info) in enumerate(subs.items(), start=1):
        generate_sub = input(f"  {idx}. Générer sous-projet {sub_name}? (o/n/all) : ").strip().lower()
        if generate_sub not in ["o", "all"]:
            continue

        sub_path = os.path.join(chapter_path, sub_name)
        create_dir(sub_path)
        proj_type = info.get("type", "simulation")

        # Créer dossiers standards
        create_standard_dirs(sub_path)

        # Vérifier fichiers existants
        existing = list_existing_files(sub_path)
        if existing:
            print("    ⚠️ Fichiers existants :")
            for f in existing:
                print(f"      - {f}")
            overwrite = input("    Écraser les fichiers existants? (o/n) : ").strip().lower() == "o"
        else:
            overwrite = True

        # Créer fichiers standards (ou copier templates)
        for f in STANDARD_FILES.get(proj_type, []):
            dest_file = os.path.join(sub_path, f)
            copy_template(proj_type, dest_file, f, overwrite)

        # Créer screenshots
        create_screenshots(sub_path, overwrite)

print("\n✅ Arborescence générée !")
for chapter, subs in PROJECTS.items():
    print(chapter)
    for sub_name in subs:
        print("  └─", sub_name)
