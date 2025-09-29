# export des données SQLite → CSV ou JSON

import sqlite3
import pandas as pd
import argparse

def export_data(db_path="data/capteurs.db", output_path="data/export_from_db.csv", format="csv"):
    # Connexion à la base SQLite
    conn = sqlite3.connect(db_path)

    # Lire toute la table 'mesures' avec pandas
    df = pd.read_sql_query("SELECT * FROM mesures ORDER BY id ASC", conn)
    conn.close()

    # Export selon le format choisi
    if format == "csv":
        df.to_csv(output_path, index=False, encoding="utf-8")
    elif format == "json":
        df.to_json(output_path, orient="records", indent=2, force_ascii=False)
    else:
        raise ValueError("Format non supporté : choisir 'csv' ou 'json'")

    print(f"✅ Données exportées vers {output_path} en format {format}")
    print(df.tail(5))  # afficher les 5 dernières lignes pour contrôle


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exporter les données SQLite vers CSV ou JSON")
    parser.add_argument("--db", default="data/capteurs.db", help="Chemin vers la base SQLite")
    parser.add_argument("--output", default="data/export_from_db.csv", help="Fichier de sortie")
    parser.add_argument("--format", default="csv", choices=["csv", "json"], help="Format d'export")

    args = parser.parse_args()
    export_data(db_path=args.db, output_path=args.output, format=args.format)
