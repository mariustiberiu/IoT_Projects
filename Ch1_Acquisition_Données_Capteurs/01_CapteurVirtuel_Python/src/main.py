import time
import random
from datetime import datetime

def generate_sensor_data():
    """
    Génère un dictionnaire avec des valeurs de capteur simulées
    """
    temperature = round(random.uniform(20.0, 30.0), 1)
    humidity = round(random.uniform(30.0, 70.0), 1)
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temperature,
        "humidity": humidity
    }

def main():
    print("=== Capteur Virtuel Python ===")
    print("Génération de données simulées toutes les 2 secondes.")
    print("Tapez Ctrl+C pour arrêter.\n")

    try:
        while True:
            data = generate_sensor_data()
            print(f"📊 Données capteur : {data}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n👋 Programme terminé.")

if __name__ == "__main__":
    main()
