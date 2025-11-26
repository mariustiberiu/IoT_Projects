import pandas as pd
import numpy as np
from datetime import datetime
import time
import os

DATA_FILE = "data/sample.csv"
os.makedirs("data", exist_ok=True)

# Si le fichier n'existe pas, crée-le avec 20 lignes de base
if not os.path.exists(DATA_FILE):
    timestamps = pd.date_range(start=datetime.now(), periods=20, freq="S")
    temperature = np.random.randint(18, 35, 20)
    humidity = np.random.randint(30, 90, 20)
    df = pd.DataFrame({"timestamp": timestamps, "temperature": temperature, "humidity": humidity})
    df.to_csv(DATA_FILE, index=False)

# Boucle infinie pour ajouter une nouvelle ligne chaque seconde
while True:
    df = pd.read_csv(DATA_FILE)
    new_row = {
        "timestamp": datetime.now(),
        "temperature": np.random.randint(18, 35),
        "humidity": np.random.randint(30, 90)
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    time.sleep(1)
