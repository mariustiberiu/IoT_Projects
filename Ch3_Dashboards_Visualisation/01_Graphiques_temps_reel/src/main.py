import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import os
from datetime import datetime
import random

# ===== Dossiers =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "sample.csv")
EXPORT_DIR = os.path.join(BASE_DIR, "..", "exports")

# Créer dossier exports s'il n'existe pas
os.makedirs(EXPORT_DIR, exist_ok=True)

# ===== Initialisation du CSV si vide =====
if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
    df_init = pd.DataFrame({
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "temperature": [20],
        "humidity": [50]
    })
    df_init.to_csv(DATA_FILE, index=False)

# ===== Lecture des données =====
def read_data():
    df = pd.read_csv(DATA_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

# ===== Ajout de nouvelles données =====
def append_new_data():
    df = read_data()
    last_time = df['timestamp'].iloc[-1]
    new_time = last_time + pd.Timedelta(seconds=2)
    new_temp = df['temperature'].iloc[-1] + random.randint(-1, 2)
    new_hum = df['humidity'].iloc[-1] + random.randint(-1, 2)
    new_row = pd.DataFrame({
        "timestamp": [new_time],
        "temperature": [new_temp],
        "humidity": [new_hum]
    })
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

# ===== Animation du graphique =====
def animate(i):
    append_new_data()  # ajoute de nouvelles données
    df = read_data()
    plt.cla()
    
    # Tracer Température et Humidité
    plt.plot(df['timestamp'], df['temperature'], marker='o', label='Température (°C)')
    plt.plot(df['timestamp'], df['humidity'], marker='x', label='Humidité (%)')
    
    plt.xlabel("Temps")
    plt.ylabel("Valeurs")
    plt.title("Température et humidité en temps réel")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.tight_layout()

    # Formater l'axe X pour les timestamps
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gcf().autofmt_xdate()  # rotation automatique

    # Export automatique
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_path = os.path.join(EXPORT_DIR, f"export_{timestamp_str}.csv")
    df.to_csv(export_path, index=False)

# ===== Lancement du graphique =====
fig = plt.figure(figsize=(10, 5))
ani = animation.FuncAnimation(fig, animate, interval=2000, cache_frame_data=False)

plt.show()  # Affiche le graphique et le met à jour toutes les 2 secondes
