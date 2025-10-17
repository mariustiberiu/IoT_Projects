import os

# Template de sous-projets (tu pourras le réutiliser pour Ch7, Ch8, etc.)
SUBPROJECT_TEMPLATE = {
    "README.md": "# {title}\n\n{description}\n",
    "src": {"{script_name}.py": "# Script pour {description}\n"},
    "data": {"{sample_file}": "{sample_content}"},
    "screenshots": {"screenshot_console_{short_name}.png": ""}
}

# Fonction pour créer un sous-projet à partir du template
def create_subproject(base_path, name, title, description, script_name, sample_file, sample_content, short_name):
    project_path = os.path.join(base_path, name)
    os.makedirs(project_path, exist_ok=True)

    for key, value in SUBPROJECT_TEMPLATE.items():
        if isinstance(value, dict):
            subdir = os.path.join(project_path, key)
            os.makedirs(subdir, exist_ok=True)
            for fname, content in value.items():
                fname = fname.format(
                    script_name=script_name,
                    short_name=short_name,
                    sample_file=sample_file
                )
                fpath = os.path.join(subdir, fname)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content.format(
                        title=title,
                        description=description,
                        script_name=script_name,
                        sample_file=sample_file,
                        sample_content=sample_content,
                        short_name=short_name
                    ))
        else:
            fpath = os.path.join(project_path, key)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(value.format(
                    title=title,
                    description=description
                ))

# Exemple d’utilisation pour recréer Ch6
if __name__ == "__main__":
    base_dir = os.path.join(os.getcwd(), "Ch6_Cloud_Edge_Computing")
    os.makedirs(base_dir, exist_ok=True)

    create_subproject(
        base_dir,
        "01_AWS_IoT_Core",
        "6.1 - AWS IoT Core",
        "Connexion et envoi de données vers AWS IoT Core",
        "aws_iot_core_client",
        "sample_aws_data.json",
        '{ "temperature": 25, "humidity": 40 }',
        "aws_iot"
    )

    create_subproject(
        base_dir,
        "02_Google_Cloud_IoT_Core",
        "6.2 - Google Cloud IoT Core",
        "Intégration avec Google Cloud IoT Core",
        "gcloud_iot_core_client",
        "sample_gcloud_data.json",
        '{ "temperature": 22, "humidity": 55 }',
        "gcloud_iot"
    )

    create_subproject(
        base_dir,
        "03_Edge_RaspberryPi",
        "6.3 - Edge Computing avec Raspberry Pi",
        "Traitement local des données sur Raspberry Pi",
        "edge_raspberrypi_processing",
        "sample_rpi_data.csv",
        "time,temperature,humidity\n2025-10-01,24,60",
        "rpi_edge"
    )

    create_subproject(
        base_dir,
        "04_Docker_IoT_Service",
        "6.4 - Déploiement IoT avec Docker",
        "Déploiement d’un service IoT sous Docker",
        "docker_iot_service",
        "docker-compose.yml",
        "version: '3'\nservices:\n  iot_service:\n    build: .\n    ports:\n      - \"5000:5000\"\n",
        "docker_iot"
    )

    print("✅ Ch6 généré automatiquement avec le template !")
