# graphique matplotlib

# src/plot_data.py
import sqlite3
import matplotlib.pyplot as plt
import argparse

def plot_from_db(db_path="data/capteurs.db", output_file="screenshots/graphique_mesures.png"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT timestamp, temperature, humidite FROM mesures ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("⚠️ La base est vide, ajoute d'abord des mesures (simulation ou Arduino).")
        return

    temps = [r[0] for r in rows]
    temperatures = [r[1] for r in rows]
    humidites = [r[2] for r in rows]

    plt.figure(figsize=(10,5))
    plt.plot(temps, temperatures, label="Température (°C)", color="red", marker="o")
    plt.plot(temps, humidites, label="Humidité (%)", color="blue", marker="x")
    plt.xlabel("Horodatage")
    plt.ylabel("Valeurs")
    plt.title("Évolution Température & Humidité")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
    print(f"✅ Graphique généré : {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="data/capteurs.db", help="Chemin vers la base SQLite")
    parser.add_argument("--output", default="screenshots/graphique_mesures.png", help="Nom du fichier PNG de sortie")
    args = parser.parse_args()

    plot_from_db(db_path=args.db, output_file=args.output)



# graphique matplotlib