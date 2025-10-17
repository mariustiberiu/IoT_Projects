"""
Simulateur temps réel pour MongoDB
Insère des documents dans la collection 'capteurs' de 'ma_base'
"""

import time
import random
from pymongo import MongoClient
from datetime import datetime, timezone

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")  # même instance que ton dashboard
db = client["ma_base"]
capteurs = db["capteurs"]

# Liste des capteurs simulés
liste_capteurs = ["sensor_1", "sensor_2", "sensor_3"]

def simulate(interval=2):
    i = 0
    while True:
        i += 1
        doc = {
            "sensor_name": random.choice(liste_capteurs),
            "temperature": round(20 + random.random() * 8, 2),
            "humidite": round(40 + random.random() * 30, 2),
            "timestamp":  datetime.now(timezone.utc)
        }
        capteurs.insert_one(doc)
        print(f"Inserted sample #{i} -> {doc}")
        time.sleep(interval)

if __name__ == "__main__":
    print("Simulation démarrée. Ctrl+C pour arrêter.")
    simulate()
