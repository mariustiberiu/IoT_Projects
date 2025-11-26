import pandas as pd
import numpy as np
import time
import os
from datetime import datetime

# --- Fichier JSON cible ---
DATA_FILE_JSON = "data/sample.json"
os.makedirs("data", exist_ok=True)

# --- Boucle de simulation ---
while True:
    # Génération d'une nouvelle ligne
    new_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": np.random.randint(18, 35),
        "humidity": np.random.randint(30, 90)
    }

    # Lecture des données existantes
    if os.path.exists(DATA_FILE_JSON):
        try:
            df = pd.read_json(DATA_FILE_JSON)
        except ValueError:
            df = pd.DataFrame(columns=["timestamp", "temperature", "humidity"])
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    # Écriture dans le JSON
    df.to_json(DATA_FILE_JSON, orient="records", date_format="iso")

    # Pause 1 seconde
    time.sleep(1)
