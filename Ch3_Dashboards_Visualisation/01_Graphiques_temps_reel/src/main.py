import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from datetime import datetime, timedelta
import random
import time

# ===== Dossiers =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "sample.csv")
EXPORT_DIR = os.path.join(BASE_DIR, "..", "exports")

# Créer dossier exports s'il n'existe pas
os.makedirs(EXPORT_DIR, exist_ok=True)

# ===== Initialisation du CSV si vide =====
if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
    df = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "temperature": [20],
        "humidity": [50]
    })
    df.to_csv(DATA_FILE, index=False)

# ===== Simulation de nouvelles données =====
def append_new_data():
    df = pd.read_csv(DATA_FILE)
    last_time = pd.to_datetime(df['timestamp'].iloc[-1])
    new_time = last_time + timedelta(seconds=2)
    new_temp = df['temperature'].iloc[-1] + random.randint(-1, 2)
    new_hum = df['humidity'].iloc[-1] + random.randint(-1, 2)
    new_row = pd.DataFrame({"timestamp":[new_time], "temperature":[new_temp], "humidity":[new_hum]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# ===== Lecture des données =====
def read_data():
    df = pd.read_csv(DATA_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# ===== Animation du graphique =====
def animate(i):
    df = read_data()
    if df.empty:
        return

    plt.cla()
    plt.plot(df['timestamp'], df['temperature'], marker='o', label='Température (°C)')
    plt.plot(df['timestamp'], df['humidity'], marker='x', label='Humidité (%)')

    plt.xlabel("Temps")
    plt.ylabel("Valeurs")
    plt.title("Température et humidité en temps réel")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.grid(True)
    plt.legend(loc="upper left")

    # Export automatique
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_path = os.path.join(EXPORT_DIR, f"export_{timestamp_str}.csv")
    df.to_csv(export_path, index=False)

# ===== Lancement graphique et simulation =====
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=2000, cache_frame_data=False)

# Boucle infinie pour ajouter des données toutes les 2 secondes
try:
    while True:
        append_new_data()
        plt.pause(2)  # Met à jour le graphique
except KeyboardInterrupt:
    print("\nProgramme arrêté.")
    plt.close('all')

