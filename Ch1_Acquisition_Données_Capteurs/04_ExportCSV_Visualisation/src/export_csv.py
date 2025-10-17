import os
import sqlite3
from datetime import datetime
import argparse

# pandas import centralisé (facile à mock si besoin)
try:
    import pandas as pd
except Exception as e:
    raise SystemExit("pandas est requis : pip install pandas") from e

import random
import time


def generate_fake_data(rows=20):
    """Génère un DataFrame simulé température/humidité"""
    data = []
    now = int(time.time())
    for i in range(rows):
        ts = datetime.fromtimestamp(now - (rows - i - 1) * 60).strftime("%Y-%m-%d %H:%M:%S")
        data.append({
            "id": i + 1,
            "timestamp": ts,
            "temperature": round(random.uniform(18.0, 30.0), 2),
            "humidity": round(random.uniform(30.0, 75.0), 2),
        })
    return pd.DataFrame(data)


def export_data(db_path="../data/capteurs.db",
                output_path="../exports/data.json",
                format="csv",
                simulate=False,
                rows=20):
    """Export : si simulate=True -> génère fake data, sinon lit la table 'mesures'"""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    if simulate:
        df = generate_fake_data(rows=rows)
        source = "SIMULATION"
    else:
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"La DB SQLite n'existe pas : {db_path}")
        conn = sqlite3.connect(db_path)
        # adapter le nom de la table si nécessaire
        df = pd.read_sql_query("SELECT * FROM mesures ORDER BY id ASC", conn)
        conn.close()
        source = f"SQLite: {db_path}"

    # export
    # export
    if format == "csv":
        df.to_csv(output_path + ".csv", index=False, encoding="utf-8")
        final_path = output_path + ".csv"
    elif format == "json":
        df.to_json(output_path + ".json", orient="records", indent=2, force_ascii=False)
        final_path = output_path + ".json"
    else:
        raise ValueError("Format non supporté : utiliser 'csv' ou 'json'")

    print(f"✅ Export ({source}) -> {final_path} ({len(df)} lignes).")# retourner le DataFrame pour utilisation ultérieure (visualisation)
    return df


def parse_cli_and_run():
    parser = argparse.ArgumentParser(description="Exporter données capteurs (SQLite ou simulation)")
    parser.add_argument("--db", default="../data/capteurs.db", help="chemin vers la base SQLite")
    parser.add_argument("--output", default="../exports/export_data", help="fichier de sortie (extension ajoutée automatiquement selon --format)")
    parser.add_argument("--format", default="csv", choices=["csv", "json"], help="format de sortie")
    parser.add_argument("--simulate", action="store_true", help="générer des données simulées")
    parser.add_argument("--rows", type=int, default=20, help="nombre de lignes si simulation")
    parser.add_argument("--interactive", action="store_true", help="mode interactif (demande si simulation)")

    args = parser.parse_args()

    simulate = args.simulate
    if args.interactive:
        # prompt interactif si demandé
        ans = input("Voulez-vous générer des données SIMULÉES au lieu d'utiliser la DB SQLite ? (o/n) : ").strip().lower()
        simulate = (ans == "o" or ans == "y")

    export_data(db_path=args.db, output_path=args.output, format=args.format, simulate=simulate, rows=args.rows)


if __name__ == "__main__":
    parse_cli_and_run()
