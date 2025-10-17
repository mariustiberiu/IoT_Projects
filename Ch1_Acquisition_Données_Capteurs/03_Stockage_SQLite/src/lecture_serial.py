# === Optionnel : Affichage des dernières mesures ===
# 1. src/lecture_serial.py – simule ou lit les mesures (température/humidité) depuis Arduino/port série.
# acquisition (Arduino ou simulation)

import argparse
import time
import random
import sqlite3
from datetime import datetime

# Vérification si pyserial est installé pour le mode Arduino
try:
    import serial
except ImportError:
    serial = None

# Connexion à SQLite
def init_db(db_path="data/capteurs.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mesures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidite REAL
        )
    """)
    conn.commit()
    return conn

def insert_mesure(conn, t, h):
    """Insère une mesure dans la base"""
    cur = conn.cursor()
    cur.execute("INSERT INTO mesures (timestamp, temperature, humidite) VALUES (?, ?, ?)",
                (datetime.now().isoformat(), t, h))
    conn.commit()

def simulation_mesures(conn, duree=10):
    """Simule les mesures de température et humidité"""
    for _ in range(duree):
        t = random.uniform(18, 30)  # Température
        h = random.uniform(40, 80)  # Humidité
        print(f"Simulation -> Temp: {t:.2f} °C, Hum: {h:.2f} %")
        insert_mesure(conn, t, h)
        time.sleep(1)

def lire_depuis_arduino(conn, port="COM3", baudrate=115200, duree=10):
    """Lit les mesures depuis Arduino"""
    if serial is None:
        print("Erreur: pyserial n'est pas installé !")
        return
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            start = time.time()
            while time.time() - start < duree:
                ligne = ser.readline().decode('utf-8').strip()
                if ligne:
                    try:
                        t, h = map(float, ligne.split(","))
                        print(f"Arduino -> Temp: {t:.2f} °C, Hum: {h:.2f} %")
                        insert_mesure(conn, t, h)
                    except Exception as e:
                        print(f"Ligne ignorée: {ligne} ({e})")
    except Exception as e:
        print(f"Erreur lors de la lecture Arduino : {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["simulation", "arduino"], default="simulation")
    parser.add_argument("--duree", type=int, default=10)
    parser.add_argument("--port", type=str, default="COM3")
    args = parser.parse_args()

    conn = init_db()

    if args.mode == "simulation":
        simulation_mesures(conn, duree=args.duree)
    else:
        lire_depuis_arduino(conn, port=args.port, duree=args.duree)

    conn.close()
# 1. src/lecture_serial.py – simule ou lit les mesures (température/humidité) depuis Arduino/port série.


