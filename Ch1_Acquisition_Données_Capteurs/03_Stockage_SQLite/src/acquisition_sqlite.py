# 2. src/acquisition_sqlite.py – crée la base SQLite data/capteurs.db et insère les mesures.


#!/usr/bin/env python3
# src/acquisition_sqlite.py
"""
Acquisition -> enregistrement SQLite
Usage examples:
  python src/acquisition_sqlite.py --mode simulation --duree 20
  python src/acquisition_sqlite.py --mode csv --csv data/sample_from_serial.csv
  python src/acquisition_sqlite.py --show-last 10
  python src/acquisition_sqlite.py --export data/export_from_db.csv
"""
import sqlite3
import argparse
import time
import random
import csv
import os
from datetime import datetime
from pathlib import Path

# Chemin par défaut de la base
ROOT = Path(__file__).resolve().parents[1]   # dossier du projet 03
DATA_DIR = ROOT / "data"
DB_FILE = DATA_DIR / "capteurs.db"
os.makedirs(DATA_DIR, exist_ok=True)

SQL_CREATE = """
CREATE TABLE IF NOT EXISTS mesures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    temperature REAL,
    humidite REAL,
    source TEXT
);
CREATE INDEX IF NOT EXISTS idx_timestamp ON mesures(timestamp);
"""

def get_conn(db_path=DB_FILE):
    conn = sqlite3.connect(str(db_path))
    return conn

def init_db(conn):
    cur = conn.cursor()
    cur.executescript(SQL_CREATE)
    conn.commit()

def insert_measure(conn, timestamp, temperature, humidite, source="simulation"):
    cur = conn.cursor()
    cur.execute("INSERT INTO mesures (timestamp, temperature, humidite, source) VALUES (?, ?, ?, ?)",
                (timestamp, temperature, humidite, source))
    conn.commit()

def simulate_to_db(conn, duree=20, delay=2.0):
    print(f"Simulation: durée={duree}s, delay={delay}s, insertion dans {DB_FILE}")
    t0 = time.time()
    while time.time() - t0 < duree:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t = round(random.uniform(18.0, 30.0), 2)
        h = round(random.uniform(40.0, 80.0), 2)
        print(f"{ts}  T={t} °C  H={h} %")
        insert_measure(conn, ts, t, h, source="simulation")
        time.sleep(delay)
    print("Simulation terminée.")

def import_csv_to_db(conn, csv_path):
    if not Path(csv_path).exists():
        print("Fichier CSV introuvable:", csv_path)
        return
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        nb = 0
        for row in reader:
            ts = row.get("timestamp") or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            t = float(row.get("temperature") or 0)
            h = float(row.get("humidite") or 0)
            insert_measure(conn, ts, t, h, source="csv")
            nb += 1
    print(f"{nb} lignes importées depuis {csv_path}.")

def show_last(conn, n=10):
    cur = conn.cursor()
    cur.execute("SELECT id, timestamp, temperature, humidite, source FROM mesures ORDER BY id DESC LIMIT ?", (n,))
    rows = cur.fetchall()
    if not rows:
        print("Aucune mesure dans la base.")
        return
    print("id | timestamp           | temp | hum | source")
    for r in rows[::-1]:  # affiche dans l'ordre chronologique
        print(r)

def export_csv(conn, out_path):
    cur = conn.cursor()
    cur.execute("SELECT timestamp, temperature, humidite, source FROM mesures ORDER BY id")
    rows = cur.fetchall()
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidite", "source"])
        writer.writerows(rows)
    print(f"Export terminé -> {out_path}")

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["simulation", "csv"], help="Source des données")
    p.add_argument("--duree", type=int, default=20, help="Durée de la simulation (s)")
    p.add_argument("--delay", type=float, default=2.0, help="Intervalle entre mesures (s)")
    p.add_argument("--csv", type=str, help="Fichier CSV à importer (si --mode csv)")
    p.add_argument("--show-last", type=int, help="Afficher N dernières mesures")
    p.add_argument("--export", type=str, help="Exporter toutes les mesures vers un CSV")
    return p.parse_args()

def main():
    args = parse_args()
    conn = get_conn()
    init_db(conn)

    if args.mode == "simulation":
        simulate_to_db(conn, duree=args.duree, delay=args.delay)
    elif args.mode == "csv":
        if not args.csv:
            print("Erreur: précisez --csv chemin_vers_fichier.csv")
        else:
            import_csv_to_db(conn, args.csv)

    if args.show_last:
        show_last(conn, args.show_last)

    if args.export:
        export_csv(conn, args.export)

    conn.close()

if __name__ == "__main__":
    main()

# 2. src/acquisition_sqlite.py – crée la base SQLite data/capteurs.db et insère les mesures.
