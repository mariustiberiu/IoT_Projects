# backup_and_export.py - Version CLI flexible
import os
import shutil
import datetime
import sqlite3
import pandas as pd
import argparse

# ------------------------------
# Paramètres
# ------------------------------
DB_FOLDER = "data"
DB_PATH = os.path.join(DB_FOLDER, "capteurs.db")

if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

# ------------------------------
# Fonctions
# ------------------------------
def create_backup(db_path=DB_PATH):
    """Crée un backup horodaté de la DB"""
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{now}.db"
    backup_path = os.path.join(DB_FOLDER, backup_name)
    shutil.copy2(db_path, backup_path)
    print(f"✅ Backup créé : {backup_path}")
    return backup_path

def export_csv(df, prefix="export"):
    """Export CSV horodaté"""
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = os.path.join(DB_FOLDER, f"{prefix}_{now}.csv")
    df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"✅ Export CSV créé : {csv_file}")
    return csv_file

def export_json(df, prefix="export"):
    """Export JSON horodaté"""
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    json_file = os.path.join(DB_FOLDER, f"{prefix}_{now}.json")
    df.to_json(json_file, orient="records", indent=4, date_format="iso")
    print(f"✅ Export JSON créé : {json_file}")
    return json_file

def read_measures(db_path=DB_PATH):
    """Lit toutes les mesures de la table"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM mesures ORDER BY id ASC", conn)
    conn.close()
    return df

# ------------------------------
# Main
# ------------------------------
def main():
    parser = argparse.ArgumentParser(description="Backup et export CSV/JSON")
    parser.add_argument("--backup", action="store_true", help="Créer un backup de la DB")
    parser.add_argument("--csv", action="store_true", help="Exporter les mesures en CSV")
    parser.add_argument("--json", action="store_true", help="Exporter les mesures en JSON")
    parser.add_argument("--all", action="store_true", help="Faire backup + CSV + JSON")
    args = parser.parse_args()

    df = read_measures()

    if args.backup or args.all:
        create_backup()
    if args.csv or args.all:
        export_csv(df)
    if args.json or args.all:
        export_json(df)

    print("🔹 5 dernières lignes du DataFrame pour contrôle :")
    print(df.tail(5))

# ------------------------------
if __name__ == "__main__":
    main()

