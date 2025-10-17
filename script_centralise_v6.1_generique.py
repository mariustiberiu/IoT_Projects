import os

# Définition des chapitres et sous-parties
structure = {
    "Ch1_Acquisition_Donnees_Capteurs": ["01_CapteurVirtuel_Python", "02_LectureSerie_PySerial"],
    "Ch2_Communication_IoT": ["01_MQTT_Base", "02_HTTP_Requetes"],
    "Ch3_Analyse_Visualisation": ["01_AnalyseCSV_Pandas", "02_Visualisation_Matplotlib"],
    "Ch4_Securite_IoT": ["01_Chiffrement_RSA", "02_Authentification_Token"],
    "Ch5_Integration_Systemes": ["01_API_Flask", "02_Monitoring_Systeme"],
    "Ch6_Cloud_Edge_Computing": ["01_Cloud_AWS_IoT", "02_Edge_RaspberryPi"]
}

# Code générique à insérer dans chaque script Python
generic_code = """# Script IoT générique
def main():
    print("👋 Hello IoT - Script générique en cours d'exécution !")

if __name__ == "__main__":
    main()
"""

for chapter, topics in structure.items():
    for topic in topics:
        base_path = os.path.join(chapter, topic)
        src_path = os.path.join(base_path, "src")
        data_path = os.path.join(base_path, "data")
        screenshots_path = os.path.join(base_path, "screenshots")

        os.makedirs(src_path, exist_ok=True)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(screenshots_path, exist_ok=True)

        # README
        readme_file = os.path.join(base_path, "README.md")
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(f"# {topic}\n\nProjet du chapitre {chapter}\n")

        # Code générique
        script_file = os.path.join(src_path, f"{topic.lower()}.py")
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(generic_code.replace("IoT - Script générique", f"IoT - {topic}"))

        # Placeholder screenshot
        screenshot_file = os.path.join(screenshots_path, f"screenshot_console_{topic}.png")
        with open(screenshot_file, "wb") as f:
            pass

print("✅ Tous les chapitres et scripts génériques ont été générés !")
