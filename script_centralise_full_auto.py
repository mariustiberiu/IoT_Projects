import os
import shutil

# ==============================
# CONFIGURATION
# ==============================
BASE_PATH = os.getcwd()
CENTRAL_COPY_FOLDER = "project_backup"

# Chapitres et sous-projets définis par ton sommaire
PROJECTS = {
    "Ch1_Acquisition_Données_Capteurs": {
        "01_CapteurVirtuel_Python": "simulation",
        "02_LectureSerie_PySerial": "arduino",
        "03_Stockage_SQLite": "simulation_ou_arduino",
        "04_ExportCSV_Visualisation": "simulation_ou_arduino"
    },
    "Ch2_Communication_MQTT_API": {
        "01_Serveur_MQTT": "simulation",
        "02_Publish_subscribe_multi_clients": "simulation",
        "03_Securisation_MQTT_SSL_TLS": "simulation",
        "04_API_REST_Django": "simulation"
    },
    "Ch3_Dashboards_Visualisation": {
        "01_Graphiques_temps_reel": "simulation",
        "02_Application_interactive_Streamlit": "simulation",
        "03_Dashboard_Django_MongoDB": "simulation",
        "04_Dashboard_Grafana_InfluxDB": "simulation"
    },
    "Ch4_Analyse_Predictive": {
        "01_Regression_lineaire": "simulation",
        "02_Series_temporelles_ARIMA": "simulation",
        "03_Detection_anomalies_IsolationForest": "simulation",
        "04_Classification_sonore": "simulation"
    },
    "Ch5_Securite_IoT": {
        "01_Auth_JWT_Django": "simulation",
        "02_Chiffrement_AES": "simulation",
        "03_Detection_intrusion_logs": "simulation"
    },
    "Ch6_Cloud_Edge": {
        "01_AWS_IoT_Core": "simulation",
        "02_Google_Cloud_IoT": "simulation",
        "03_Edge_RaspberryPi": "simulation",
        "04_Deploy_Docker": "simulation"
    },
    "Ch7_Projets_Avances_IA": {
        "01_Reconnaissance_images": "simulation",
        "02_Detection_evenements_audio": "simulation",
        "03_Systeme_recommandation": "simulation",
        "04_Projet_final_SmartHome": "simulation_ou_arduino"
    }
}

# Dossiers standards pour chaque sous-projet
STANDARD_DIRS = ["src", "data", "backup", "exports", "screenshots"]

# Fichiers standards selon type
STANDARD_FILES = {
    "simulation": [
        "src/main.py",
        "data/sample.csv",
        "data/sample.json",
        "screenshots/screenshot_01.png",
        "screenshots/screenshot_02.png",
    ],
    "arduino": [
        "src/main.py",
        "arduino/project.ino",
        "data/sample.csv",
        "screenshots/screenshot_01.png",
    ],
    "simulation_ou_arduino": [
        "src/main.py",
        "arduino/project.ino",
        "data/sample.csv",
        "data/sample.json",
        "screenshots/screenshot_01.png",
        "screenshots/screenshot_02.png",
    ]
}


# ==============================
# UTILITAIRES
# ==============================
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_file(path):
    """Crée un fichier vide s'il n'existe pas déjà"""
    if not os.path.exists(path):
        ensure_dir(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            f.write("")

def build_structure():
    """Créer tous les dossiers/fichiers selon PROJECTS"""
    for chapter, subs in PROJECTS.items():
        for sub, proj_type in subs.items():
            proj_path = os.path.join(BASE_PATH, chapter, sub)
            ensure_dir(proj_path)

            # Dossiers standards
            for d in STANDARD_DIRS:
                ensure_dir(os.path.join(proj_path, d))

            # Fichiers standards
            for f in STANDARD_FILES.get(proj_type, []):
                ensure_file(os.path.join(proj_path, f))


def copy_files(src_folder, dst_folder):
    """Copie tous les fichiers utiles dans le backup central"""
    ensure_dir(dst_folder)
    for root, dirs, files in os.walk(src_folder):
        for f in files:
            ext = os.path.splitext(f)[1]
            if ext in {".py", ".csv", ".json", ".db", ".png", ".ino"}:
                src_path = os.path.join(root, f)
                rel_path = os.path.relpath(src_path, src_folder)
                dst_path = os.path.join(dst_folder, rel_path)
                ensure_dir(os.path.dirname(dst_path))
                shutil.copy2(src_path, dst_path)


def build_tree(root, prefix=""):
    """Construit une représentation arborescente style tree"""
    lines = []
    items = sorted(os.listdir(root))
    for i, item in enumerate(items):
        connector = "└─ " if i == len(items) - 1 else "├─ "
        path = os.path.join(root, item)
        lines.append(prefix + connector + item)
        if os.path.isdir(path):
            extension = "   " if i == len(items) - 1 else "│  "
            lines.extend(build_tree(path, prefix + extension))
    return lines


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    print("🚀 Génération de l’arborescence complète...")
    build_structure()

    # Backup central
    ensure_dir(CENTRAL_COPY_FOLDER)
    for chapter in PROJECTS:
        src_folder = os.path.join(BASE_PATH, chapter)
        dst_folder = os.path.join(CENTRAL_COPY_FOLDER, chapter)
        copy_files(src_folder, dst_folder)

    # Génération du tree
    tree_lines = []
    for chapter in PROJECTS:
        chapter_path = os.path.join(BASE_PATH, chapter)
        if os.path.exists(chapter_path):
            tree_lines.append(chapter + "/")
            tree_lines.extend(build_tree(chapter_path, "   "))

    # Sauvegarde markdown
    md_file = os.path.join(BASE_PATH, "project_tree.md")
    with open(md_file, "w", encoding="utf-8") as f:
        f.write("\n".join(tree_lines))

    print("\n✅ Structure générée et fichiers créés")
    print(f"✅ Backup central dans {CENTRAL_COPY_FOLDER}/")
    print(f"✅ Arborescence enregistrée dans {md_file}")
