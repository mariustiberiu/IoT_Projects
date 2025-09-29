# La création automatique de la table mesures si elle n’existe pas.

# La vérification et création automatique de la colonne source.

# La simulation avec insertion des mesures dans SQLite.

import sqlite3
import os
import time
import random
from datetime import datetime
import argparse
import csv

# ------------------------------
# Paramètres
# ------------------------------
db_folder = "data"
db_path = os.path.join(db_folder, "capteurs.db")
csv_backup_path = os.path.join(db_folder, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")

# Crée le dossier data si inexistant
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

# ------------------------------
# Vérification / Création table
# ------------------------------
def ensure_table(conn):
    cur = conn.cursor()
    # Crée la table si elle n'existe pas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mesures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidite REAL
        )
    """)
    conn.commit()

    # Vérifie si la colonne 'source' existe
    cur.execute("PRAGMA table_info(mesures)")
    columns = [col[1] for col in cur.fetchall()]
    if "source" not in columns:
        cur.execute("ALTER TABLE mesures ADD COLUMN source TEXT")
        conn.commit()
        print("Colonne 'source' ajoutée automatiquement !")

# ------------------------------
# Insertion d'une mesure dans DB et CSV
# ------------------------------
def insert_measure(conn, timestamp, temperature, humidite, source="simulation"):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO mesures (timestamp, temperature, humidite, source) VALUES (?, ?, ?, ?)",
        (timestamp, temperature, humidite, source)
    )
    conn.commit()
    
    # Sauvegarde dans CSV
    file_exists = os.path.isfile(csv_backup_path)
    with open(csv_backup_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "temperature", "humidite", "source"])  # en-tête
        writer.writerow([timestamp, f"{temperature:.2f}", f"{humidite:.2f}", source])
    
    # Affiche en direct
    print(f"Inséré -> {timestamp} | T={temperature:.2f}°C | H={humidite:.2f}% | source={source}")

# ------------------------------
# Simulation
# ------------------------------
def simulate_to_db(conn, duree=15, delay=2.0):
    start = time.time()
    while time.time() - start < duree:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t = random.uniform(20.0, 30.0)
        h = random.uniform(40.0, 80.0)
        insert_measure(conn, ts, t, h)
        time.sleep(delay)

# ------------------------------
# Main
# ------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["simulation"], default="simulation")
    parser.add_argument("--duree", type=int, default=15, help="Durée de la simulation (s)")
    parser.add_argument("--delay", type=float, default=2.0, help="Intervalle entre mesures (s)")
    args = parser.parse_args()

    conn = sqlite3.connect(db_path)
    ensure_table(conn)

    if args.mode == "simulation":
        print(f"Simulation: durée={args.duree}s, delay={args.delay}s, insertion dans {db_path}")
        print(f"Backup CSV: {csv_backup_path}")
        simulate_to_db(conn, duree=args.duree, delay=args.delay)

    conn.close()

if __name__ == "__main__":
    main()


# La colonne source sera automatiquement créée si elle manque.

# # Les mesures simulées sont insérées correctement dans la DB.
# Sauvegarde automatique dans un fichier CSV en plus de la DB, pour garder un backup lisible.

# Le CSV est créé dans le même dossier data et nommé automatiquement avec la date/heure.

# Les mesures simulées sont affichées en direct.

# ✅ Points forts de cette version :

# 1 Table SQLite auto-créée si manquante.

# 2 Colonne source ajoutée automatiquement si absente.

# 3 Les mesures simulées sont insérées dans la DB et sauvegardées dans un CSV pour backup ou traitement externe.

# 4 Affichage des mesures en temps réel pour suivi.

# 5 Nom CSV unique basé sur date/heure → pas de risque d’écraser les anciens backups.