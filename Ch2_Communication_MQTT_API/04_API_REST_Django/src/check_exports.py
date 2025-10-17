import csv
import json
from pathlib import Path
from tabulate import tabulate

# 🔹 Chemins corrigés pour ton projet REST
CSV_PATH = Path("../exports/mqtt_api_data.csv")
JSON_PATH = Path("../exports/mqtt_api_data.json")
N = 5  # Nombre de derniers messages à afficher

def quick_csv_check():
    if not CSV_PATH.exists():
        print("⚠️ Fichier CSV non trouvé :", CSV_PATH)
        return
    
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        print(f"\n=== Vérification CSV ({len(reader)} lignes) ===")
        if reader:
            print(tabulate(reader[-N:], headers="keys", tablefmt="grid"))
        else:
            print("📄 CSV vide")

def quick_json_check():
    if not JSON_PATH.exists():
        print("⚠️ Fichier JSON non trouvé :", JSON_PATH)
        return
    
    with open(JSON_PATH, encoding='utf-8') as f:
        data = json.load(f)
        print(f"\n=== Vérification JSON ({len(data)} éléments) ===")
        if data:
            print(tabulate(data[-N:], headers="keys", tablefmt="grid"))
        else:
            print("📄 JSON vide")

if __name__ == "__main__":
    quick_csv_check()
    quick_json_check()
