# src/main.py
import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
import random
import time

# ===== Dossiers =====
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "sample.csv")
EXPORT_DIR = os.path.join(BASE_DIR, "..", "exports")

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

# ===== Titre Streamlit =====
st.title("Dashboard Température & Humidité - Streamlit")

# ===== Affichage dynamique =====
placeholder = st.empty()

# Boucle simulation + affichage
for i in range(50):  # 50 itérations pour la démo
    append_new_data()
    df = pd.read_csv(DATA_FILE)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    with placeholder.container():
        st.subheader("Données actuelles")
        st.write(df.tail(5))  # affiche les 5 dernières lignes

        st.subheader("Graphique Température / Humidité")
        st.line_chart(df.set_index('timestamp')[['temperature', 'humidity']])

    time.sleep(2)  # délai 2 secondes pour simuler temps réel
