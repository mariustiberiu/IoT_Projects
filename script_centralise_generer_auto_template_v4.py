# script_centralise_generer_auto_template_v4.py de manière flexible :

# 1 Tous tes chapitres et sous-chapitres sont exactement comme ton sommaire.
# 2 Tous les dossiers standards (src, data, backup, exports, screenshots) sont créés automatiquement.
# 3 Les fichiers .py, .ino, .csv, .json, .md sont créés même vides.
# 4 Les screenshots sont déjà nommés screenshot_console_01.png, screenshot_console_02.png.
# 5 Option de templates : si un fichier modèle existe dans TEMPLATES/<type>/, il sera copié automatiquement.
# 6 Résumé clair à la fin pour vérifier ce qui a été créé.


# Il créera tous les dossiers et fichiers standards pour tous tes chapitres/sub-projets, même vides.
# Il copiera automatiquement les templates uniquement s’ils existent dans TEMPLATES/<type>/.
# Si pour un sous-projet tu n’as pas de template (par ex. la plupart des chapitres IoT simples), il créera juste des fichiers vides.
# Tu pourras ajouter les templates plus tard pour Django, API, ou tout autre projet spécifique.
# 🚀 Fonctionnement proposé :
# Tu crées un dossier TEMPLATES à la racine de IoT_Projects.
# Dedans, tu mets des fichiers modèles pour chaque type de projet :
# simulation/main.py
# arduino/main.ino
# simulation_ou_arduino/main.py
# Et si tu veux, d’autres fichiers .py ou .ino spécifiques.
# Le script va copier automatiquement ces fichiers dans chaque sous-projet correspondant au lieu de créer un fichier vide.
# Exemple de modification dans le script
# On ajoute une fonction copy_template :

# TEMPLATES_DIR = os.path.join(BASE_DIR, "TEMPLATES")

# def copy_template(proj_type, dest_path, filename):
#     template_path = os.path.join(TEMPLATES_DIR, proj_type, os.path.basename(filename))
#     if os.path.exists(template_path):
#         shutil.copy(template_path, dest_path)
#     else:
#         # Si le template n'existe pas, créer fichier vide
#         create_file(dest_path)


# Puis, dans la boucle où on crée les fichiers standards :

# for f in STANDARD_FILES.get(proj_type, []):
#     file_path = os.path.join(sub_path, f)
#     create_dir(os.path.dirname(file_path))
#     copy_template(proj_type, file_path, f)


# ✅ Avec ça :

# Si tu as un template pour main.py ou main.ino, il sera copié automatiquement.

# Sinon, le fichier vide sera créé comme avant.

# On peut facilement étendre à d’autres fichiers types ou même des fichiers .md ou .json.


######

# ajouter/améliorer pour les templates Django/API

# 1 Sous-projet Django/API (Ch2_04_API_REST_Django, Ch3_03_Dashboard_Django_MongoDB, etc.)
# Actuellement, le type est "simulation". Pour les sous-projets Django/API, tu peux soit :

# Mettre type="django_api" et créer un dossier TEMPLATES/django_api/ avec les fichiers main.py, urls.py, views.py, requirements.txt, README.md.
# Modifier la fonction copy_template() pour copier ces fichiers automatiquement dans le sous-projet.

# 2 Créer automatiquement les fichiers backup et exports avec timestamp
# Pour l’instant, les dossiers sont créés, mais les fichiers backup_YYYYMMDD_HHMMSS.* et export_YYYYMMDD_HHMMSS.* ne sont pas générés. On peut ajouter cette partie pour qu’ils soient prêts à l’usage.

# 3 Afficher un résumé plus détaillé
# Par exemple :

# Les dossiers créés
# Les fichiers créés
# Les templates copiés


# Gère les sous-projets Django/API avec les templates correspondants.
# Crée les fichiers backup/exports avec timestamp.
# Affiche un résumé clair pour chaque sous-chapitre.

# version améliorée de script_centralise_generer_auto_template_v5.py qui inclut :

# Gestion automatique des sous-projets Django/API avec templates spécifiques.
# Création de fichiers backup et exports avec timestamp.
# Résumé détaillé de tout ce qui a été créé (dossiers, fichiers, templates).


✅ Ce que fait ce script maintenant :

# 1 Crée tous les chapitres et sous-chapitres avec les noms exacts.
# 2 Crée les dossiers src, data, backup, exports, screenshots.
# 3 Crée les fichiers standards selon le type (simulation, arduino, simulation_ou_arduino, django_api).
# 4 Génère les screenshots screenshot_console_01.png et screenshot_console_02.png.
# 5 Crée automatiquement un fichier backup et un fichier export avec timestamp dans chaque sous-projet.
# 6 Copie les templates si disponibles dans TEMPLATES/<type>/.
# 7 Affiche un résumé clair de tout ce qui a été généré.


# Si tu appuies sur o :

# Il va créer ou compléter tous les dossiers et fichiers pour Ch1_Acquisition_Données_Capteurs (donc tous les sous-chapitres 01 → 04).
# Les autres chapitres ne seront pas touchés tant que tu ne les valides pas dans l’interactif.
# Les fichiers existants ne seront pas remplacés, le script ajoute seulement ce qui manque (dossiers, fichiers vides ou templates, screenshots).

# Donc tu peux rester à la racine et appuyer sur o sans risque de perdre ton travail actuel.

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
    "django_api": ["src/manage.py", "src/urls.py", "src/views.py", "requirements.txt", "README.md"]
}

# Dossier templates (optionnel)
TEMPLATES_DIR = os.path.join(BASE_DIR, "TEMPLATES")

# --------------------------------
# Sommaire complet (Ch1 → Ch7 et sous-chapitres)
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
        "04_API_REST_Django": {"type": "django_api"},
    },
    "Ch3_Dashboards_Visualisation": {
        "01_Graphiques_temps_reel": {"type": "simulation"},
        "02_Application_interactive_Streamlit": {"type": "simulation"},
        "03_Dashboard_Django_MongoDB": {"type": "django_api"},
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
        print(f"📁 Dossier créé : {path}")

def create_file(path):
    if not os.path.exists(path):
        create_dir(os.path.dirname(path))
        with open(path, "w", encoding="utf-8") as f:
            pass  # fichier vide
        print(f"📄 Fichier créé : {path}")

def copy_template(proj_type, dest_path, filename):
    template_path = os.path.join(TEMPLATES_DIR, proj_type, os.path.basename(filename))
    if os.path.exists(template_path):
        create_dir(os.path.dirname(dest_path))
        shutil.copy(template_path, dest_path)
        print(f"📄 Template copié : {dest_path}")
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

def create_backup_export_files(proj_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(proj_path, "backup", f"backup_{timestamp}.db")
    export_file = os.path.join(proj_path, "exports", f"export_{timestamp}.csv")
    create_file(backup_file)
    create_file(export_file)

# --------------------------------
# Génération de l’arborescence complète
# --------------------------------
for chapter, subs in PROJECTS.items():
    chapter_path = os.path.join(BASE_DIR, chapter)
    create_dir(chapter_path)
    for sub_name, info in subs.items():
        sub_path = os.path.join(chapter_path, sub_name)
        create_dir(sub_path)
        proj_type = info.get("type", "simulation")

        # Créer dossiers standards
        create_standard_dirs(sub_path)

        # Créer fichiers standards ou copier templates
        for f in STANDARD_FILES.get(proj_type, []):
            dest_file = os.path.join(sub_path, f)
            copy_template(proj_type, dest_file, f)

        # Créer screenshots
        create_screenshots(sub_path)

        # Créer fichiers backup et export avec timestamp
        create_backup_export_files(sub_path)

# --------------------------------
# Résumé final
# --------------------------------
print("\n✅ Arborescence complète générée ! Résumé :\n")
for chapter, subs in PROJECTS.items():
    print(chapter)
    for sub_name, info in subs.items():
        print(f"  └─ {sub_name} (type: {info.get('type')})")

################

# Voici une proposition de structure :

# IoT_Projects/
# │
# ├─ TEMPLATES/
# │   ├─ simulation/
# │   │   ├─ main.py
# │   │   ├─ sample.csv
# │   │   └─ sample.json
# │   │
# │   ├─ arduino/
# │   │   └─ main.ino
# │   │
# │   └─ simulation_ou_arduino/
# │       ├─ main.py
# │       ├─ sample.csv
# │       └─ sample.json
# │
# ├─ Ch1_Acquisition_Données_Capteurs/
# ├─ Ch2_Communication_MQTT_API/
# └─ … (autres chapitres)

# Explications :

# 1 TEMPLATES/simulation/
# Contient des fichiers modèles pour les sous-projets de type simulation.
# Par exemple : un main.py générique, un sample.csv vide ou avec des colonnes types, un sample.json avec structure de données de test.

# 2 TEMPLATES/arduino/
# Contient les fichiers .ino modèles pour les projets Arduino.

# 3 TEMPLATES/simulation_ou_arduino/
# Pour les sous-projets mixtes : simulation ou Arduino. Peut contenir les mêmes fichiers que simulation, éventuellement .ino si nécessaire.

# 4 Comment le script utilise ces templates
# Si un fichier existe dans TEMPLATES/<type>/nom_fichier, il sera copié dans le sous-projet correspondant.
# Sinon, un fichier vide sera créé automatiquement.

# 5 Avantage
# Tu peux préparer des fichiers de base pour Django/API (main.py, settings.py, urls.py) dans TEMPLATES/simulation/ par exemple.
# Quand tu génères l’arborescence avec le script, ces fichiers modèles seront automatiquement copiés, sans avoir besoin de créer manuellement.

# exemple concret de template pour un sous-projet Django/API, avec les fichiers main.py, urls.py, views.py, requirements.txt, prêts à être copiés dans le sous-projet correspondant.
# exemple concret de template pour un sous-projet Django/API que tu peux mettre dans ton dossier TEMPLATES/simulation/ ou créer un sous-dossier spécifique TEMPLATES/django_api/ si tu veux distinguer les templates Django.

# Structure du template
# TEMPLATES/
# └─ django_api/
#     ├─ main.py          # fichier principal pour lancer le projet ou serveur
#     ├─ requirements.txt # packages nécessaires
#     ├─ urls.py          # routes de l’API
#     ├─ views.py         # logique des endpoints
#     └─ README.md        # explications sur ce sous-projet

# Contenu des fichiers

# 1. main.py

# # main.py
# # Point d'entrée pour le sous-projet Django/API

# import os
# import sys

# def run():
#     print("Ce template est prêt pour un projet Django/API.")
#     # Ici tu peux ajouter la logique pour lancer le serveur Django ou l'API

# if __name__ == "__main__":
#     run()


# 2. requirements.txt

# Django>=4.2
# djangorestframework
# paho-mqtt


# 3. urls.py

# # urls.py
# from django.urls import path
# from .views import sample_endpoint

# urlpatterns = [
#     path('api/sample/', sample_endpoint),
# ]


# 4. views.py

# # views.py
# from django.http import JsonResponse

# def sample_endpoint(request):
#     return JsonResponse({"message": "Hello, API template is working!"})


# 5. README.md

# # Template Django/API

# Ce sous-projet est un template pour démarrer rapidement un projet Django avec REST API.
# - main.py : point d'entrée
# - urls.py : définition des routes
# - views.py : logique des endpoints
# - requirements.txt : packages nécessaires

# Comment intégrer dans ton script

# 1 Crée le dossier TEMPLATES/django_api/ dans IoT_Projects.
# 2 Copie tous ces fichiers dedans.
# 3 Dans ton script_centralise_generer_auto_template_v4.py, ajoute une étape :

# # Exemple de copie automatique des templates
# import shutil

# def copy_template(subproject_dir, project_type):
#     template_dir = os.path.join(BASE_DIR, "TEMPLATES", project_type)
#     if os.path.exists(template_dir):
#         for file_name in os.listdir(template_dir):
#             src_file = os.path.join(template_dir, file_name)
#             dst_file = os.path.join(subproject_dir, file_name)
#             if not os.path.exists(dst_file):
#                 shutil.copy2(src_file, dst_file)


# 4 Appelle cette fonction pour les sous-projets Django/API.
# Exemple :

# subproject_dir = os.path.join(BASE_DIR, "Ch2_Communication_MQTT_API", "04_API_REST_Django")
# copy_template(subproject_dir, "django_api")

# modifier directement ton script script_centralise_generer_auto_template_v4.py pour qu’il intègre automatiquement la copie des templates Django/API pour les sous-projets concernés, sans rien toucher manuellement.