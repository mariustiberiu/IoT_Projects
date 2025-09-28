# graphique matplotlib

import pandas as pd
import matplotlib.pyplot as plt

def plot_data(csv_path="data/export_from_db.csv"):
    # Charger le CSV avec pandas
    df = pd.read_csv(csv_path)

    if df.empty:
        print("⚠️ Pas de données à afficher.")
        return
    
    # Tracer température et humidité
    plt.figure(figsize=(10, 5))
    plt.plot(df["temps"], df["temperature"], label="Température (°C)", color="red", marker="o")
    plt.plot(df["temps"], df["humidite"], label="Humidité (%)", color="blue", marker="x")
    
    plt.xlabel("Temps")
    plt.ylabel("Valeurs")
    plt.title("Évolution Température / Humidité")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    # Sauvegarder une image dans screenshots/
    output_img = "screenshots/graphique_mesures.png"
    plt.savefig(output_img)
    
    print(f"✅ Graphique sauvegardé dans {output_img}")
    plt.show()

if __name__ == "__main__":
    plot_data()

# graphique matplotlib