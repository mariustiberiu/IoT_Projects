# Fonctionnalités principales :

# Arborescence complète pour chaque sous-projet, même si les fichiers ne sont pas encore écrits.

# Dossiers standards : src, data, backup, exports, screenshots.

# Fichiers standards (main.py ou .ino, sample.csv, sample.json, README.md) créés automatiquement.

# Screenshots avec noms exactement prédéfinis (screenshot_console_01.png, screenshot_console_02.png) pour que tu puisses faire tes captures sans te tromper.

# Backup et exports créés avec timestamps.

# Copie automatique depuis un modèle si MODELE existe pour éviter de réécrire des fichiers répétitifs.

# Génère un dictionnaire PROJECTS complet avec type et fichiers pour chaque sous-projet.

import os
import shutil
from datetime import datetime

# --------------------------------
# Configuration générale
# --------------------------------
BASE_DIR = os.path.abspath(".")  # Racine du projet IoT_Projects

# Fichiers standards par type de sous-projet
STANDARD_FILES = {
    "simulation": ["src/main.py", "data/sample.csv", "data/sample.json", "README.md"],
    "arduino": ["src/main.ino", "data/sample.csv", "README.md"],
    "simulation_ou_arduino": ["src/main.py", "data/sample.csv", "data/sample.json", "README.md"],
}

# Dossiers standard
STANDARD_DIRS = ["src", "data", "backup", "exports", "screenshots"]

# Screenshots par sous-projet
NUM_SCREENSHOTS = 2

# Modèles à copier (optionnel)
MODEL_DIR = os.path.join(BASE_DIR, "MODELE")  # si tu veux copier des fichiers d’un modèle

# --------------------------------
# Fonctions utilitaires
# --------------------------------
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Créé le dossier: {path}")

def create_file(path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")  # fichier vide
        print(f"Créé le fichier: {path}")

def generate_screenshots(screenshots_dir, prefix="screenshot_console", count=NUM_SCREENSHOTS):
    for i in range(1, count + 1):
        file_path = os.path.join(screenshots_dir, f"{prefix}_{i:02d}.png")
        create_file(file_path)
        print(f"Ajout screenshot: {file_path}")

def generate_backup_export_files(subproject_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(subproject_path, "backup", f"backup_{timestamp}.db")
    export_file = os.path.join(subproject_path, "exports", f"export_{timestamp}.csv")
    create_file(backup_file)
    create_file(export_file)
    return backup_file, export_file

# --------------------------------
# Détection des chapitres et sous-chapitres
# --------------------------------
PROJECTS = {}

for chapter_name in sorted(os.listdir(BASE_DIR)):
    chapter_path = os.path.join(BASE_DIR, chapter_name)
    if os.path.isdir(chapter_path) and chapter_name.startswith("Ch"):
        PROJECTS[chapter_name] = {}
        for subproject_name in sorted(os.listdir(chapter_path)):
            subproject_path = os.path.join(chapter_path, subproject_name)
            if os.path.isdir(subproject_path):
                # Déterminer type par convention
                if "Arduino" in subproject_name or "PySerial" in subproject_name:
                    proj_type = "arduino"
                elif "simulation" in subproject_name.lower():
                    proj_type = "simulation"
                else:
                    proj_type = "simulation_ou_arduino"

                PROJECTS[chapter_name][subproject_name] = {
                    "type": proj_type,
                    "files": []
                }

                # Créer les dossiers standards
                for d in STANDARD_DIRS:
                    create_dir(os.path.join(subproject_path, d))

                # Créer les fichiers standards
                for f in STANDARD_FILES[proj_type]:
                    file_path = os.path.join(subproject_path, f)
                    create_dir(os.path.dirname(file_path))
                    create_file(file_path)
                    PROJECTS[chapter_name][subproject_name]["files"].append(f)

                # Générer les screenshots avec nom spécifique
                screenshots_dir = os.path.join(subproject_path, "screenshots")
                generate_screenshots(screenshots_dir)
                for i in range(1, NUM_SCREENSHOTS + 1):
                    PROJECTS[chapter_name][subproject_name]["files"].append(f"screenshots/screenshot_console_{i:02d}.png")

                # Générer fichiers backup et export
                backup_file, export_file = generate_backup_export_files(subproject_path)
                PROJECTS[chapter_name][subproject_name]["files"].append(os.path.relpath(backup_file, subproject_path))
                PROJECTS[chapter_name][subproject_name]["files"].append(os.path.relpath(export_file, subproject_path))

                # Copier modèle si MODEL_DIR existe
                if os.path.exists(MODEL_DIR):
                    for item in os.listdir(MODEL_DIR):
                        src_item = os.path.join(MODEL_DIR, item)
                        dst_item = os.path.join(subproject_path, item)
                        if os.path.isfile(src_item):
                            shutil.copy2(src_item, dst_item)
                            PROJECTS[chapter_name][subproject_name]["files"].append(item)

# --------------------------------
# Affichage final
# --------------------------------
print("\n=== Arborescence des projets générée automatiquement ===")
for ch, subs in PROJECTS.items():
    print(f"{ch}:")
    for sub, info in subs.items():
        print(f"  {sub} ({info['type']}):")
        for f in info["files"]:
            print(f"    - {f}")
