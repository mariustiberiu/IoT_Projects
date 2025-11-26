import pandas as pd
import numpy as np
from datetime import datetime
import time
import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

CSV_FILE = os.path.join(DATA_DIR, "sample.csv")
JSON_FILE = os.path.join(DATA_DIR, "sample.json")

# Initialise fichiers si inexistants
if not os.path.exists(CSV_FILE) or not os.path.exists(JSON_FILE):
    timestamps = pd.date_range(start=datetime.now(), periods=20, freq="S")
    temperature = np.random.randint(18, 35, 20)
    humidity = np.random.randint(30, 90, 20)
    df = pd.DataFrame({"timestamp": timestamps, "temperature": temperature, "humidity": humidity})
    df.to_csv(CSV_FILE, index=False)
    df.to_json(JSON_FILE, orient="records", date_format="iso")

while True:
    df = pd.read_csv(CSV_FILE)
    new_row = {
        "timestamp": datetime.now().isoformat(),
        "temperature": np.random.randint(18, 35),
        "humidity": np.random.randint(30, 90)
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    df.to_json(JSON_FILE, orient="records", date_format="iso")
    time.sleep(1)
