 # export des données SQLite → CSV

import sqlite3
import pandas as pd

def export_csv(db_path="data/capteurs.db", csv_path="data/export_from_db.csv"):
    # Connexion à la base SQLite
    conn = sqlite3.connect(db_path)
    
    # Lire toute la table 'mesures' avec pandas
    df = pd.read_sql_query("SELECT * FROM mesures ORDER BY id ASC", conn)
    conn.close()
    
    # Sauvegarde en CSV
    df.to_csv(csv_path, index=False, encoding="utf-8")
    
    print(f"✅ Données exportées vers {csv_path}")
    print(df.tail(5))  # afficher les 5 dernières lignes pour contrôle

if __name__ == "__main__":
    export_csv()

# export des données SQLite → CSV