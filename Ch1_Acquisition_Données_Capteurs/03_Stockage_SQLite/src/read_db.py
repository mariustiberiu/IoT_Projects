# 3. src/read_db.py – pour lire les dernières mesures ou exporter vers CSV.

import sqlite3

def lire_mesures(db_path="data/capteurs.db", limit=10):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM mesures ORDER BY id DESC LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()

    print("Dernières mesures en base :")
    print("ID | Timestamp           | Température (°C) | Humidité (%)")
    print("-" * 60)
    for row in rows:
        print(f"{row[0]:<2} | {row[1]:<19} | {row[2]:<15.2f} | {row[3]:<10.2f}")

if __name__ == "__main__":
    lire_mesures()

# 3. src/read_db.py – pour lire les dernières mesures ou exporter vers CSV.
