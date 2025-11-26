import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime
from streamlit_autorefresh import st_autorefresh  # pip install streamlit-autorefresh

# --- Configuration de la page ---
st.set_page_config(page_title="Dashboard Température & Humidité", layout="wide")

# --- Auto-refresh toutes les 1 seconde ---
st_autorefresh(interval=1000, key="auto_refresh")

# --- Widgets ---
st.title("Dashboard Température & Humidité - Streamlit")

col1, col2, col3 = st.columns(3)
with col1:
    capteur = st.selectbox("Choisir le capteur à afficher :", ["Température", "Humidité"])
with col2:
    export_format = st.radio("Format d’export :", ["CSV", "JSON"])
with col3:
    data_format = st.radio("Format des données :", ["CSV", "JSON"])

st.write("Capteur sélectionné :", capteur)

# --- Placeholders ---
placeholder_graph = st.empty()
placeholder_table = st.empty()
placeholder_message = st.empty()

# --- Fichiers ---
DATA_FILE_CSV = "data/sample.csv"
DATA_FILE_JSON = "data/sample.json"
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

# --- Export bouton ---
export_button = st.button("Exporter", key="export_button")

# --- Lecture des données ---
if data_format == "CSV" and os.path.exists(DATA_FILE_CSV):
    df = pd.read_csv(DATA_FILE_CSV)
elif data_format == "JSON" and os.path.exists(DATA_FILE_JSON):
    try:
        df = pd.read_json(DATA_FILE_JSON)
    except ValueError:
        df = pd.DataFrame(columns=["timestamp", "temperature", "humidity"])
else:
    df = pd.DataFrame(columns=["timestamp", "temperature", "humidity"])

# --- Affichage graphique et tableau ---
if df.empty:
    placeholder_message.warning("⚠️ En attente de données…")
    placeholder_graph.empty()
    placeholder_table.empty()
else:
    placeholder_message.empty()
    if capteur == "Température":
        placeholder_graph.line_chart(df.set_index("timestamp")[["temperature"]])
    else:
        placeholder_graph.line_chart(df.set_index("timestamp")[["humidity"]])
    placeholder_table.dataframe(df.tail(10))

# --- Export ---
if export_button and not df.empty:
    filename_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    if export_format == "CSV":
        export_path = os.path.join(EXPORT_DIR, f"export_{filename_time}.csv")
        df.to_csv(export_path, index=False)
    else:
        export_path = os.path.join(EXPORT_DIR, f"export_{filename_time}.json")
        df.to_json(export_path, orient="records")
    st.success(f"✅ Fichier exporté : {export_path}")
