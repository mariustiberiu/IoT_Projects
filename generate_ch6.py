import os

# Définition de la structure du chapitre 6 avec noms explicites
structure = {
    "Ch6_Cloud_Edge_Computing": {
        "README.md": "# Chapitre 6 - Cloud et Edge Computing\n\nCe chapitre couvre l’intégration IoT avec le cloud et l’edge computing.",

        "01_AWS_IoT_Core": {
            "README.md": "# 6.1 - AWS IoT Core\n\nExemple d’envoi de données vers AWS IoT Core.",
            "src": {"aws_iot_core_client.py": "# Script pour connecter un capteur à AWS IoT Core\n"},
            "data": {"sample_aws_data.json": "{ \"temperature\": 25, \"humidity\": 40 }"},
            "screenshots": {"screenshot_console_aws_iot.png": ""}
        },

        "02_Google_Cloud_IoT_Core": {
            "README.md": "# 6.2 - Google Cloud IoT Core\n\nExemple d’intégration avec Google Cloud IoT Core.",
            "src": {"gcloud_iot_core_client.py": "# Script pour connecter un capteur à Google Cloud IoT Core\n"},
            "data": {"sample_gcloud_data.json": "{ \"temperature\": 22, \"humidity\": 55 }"},
            "screenshots": {"screenshot_console_gcloud_iot.png": ""}
        },

        "03_Edge_RaspberryPi": {
            "README.md": "# 6.3 - Edge computing avec Raspberry Pi\n\nExemple de traitement local avec un Raspberry Pi.",
            "src": {"edge_raspberrypi_processing.py": "# Script de traitement local sur Raspberry Pi\n"},
            "data": {"sample_rpi_data.csv": "time,temperature,humidity\n2025-10-01,24,60"},
            "screenshots": {"screenshot_console_rpi_edge.png": ""}
        },

        "04_Docker_IoT_Service": {
            "README.md": "# 6.4 - Déploiement IoT avec Docker\n\nExemple de service IoT packagé dans Docker.",
            "src": {"docker_iot_service.py": "# Exemple de service IoT avec Docker\n"},
            "data": {"docker-compose.yml": "version: '3'\nservices:\n  iot_service:\n    build: .\n    ports:\n      - \"5000:5000\"\n"},
            "screenshots": {"screenshot_console_docker_iot.png": ""}
        }
    }
}

# Fonction récursive pour créer la structure
def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

# Exécution
base_dir = os.getcwd()
create_structure(base_dir, structure)

print("✅ Chapitre 6 créé avec des noms explicites pour scripts et screenshots.")
