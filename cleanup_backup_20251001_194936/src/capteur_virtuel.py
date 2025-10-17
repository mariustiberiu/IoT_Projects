import random
import time
import csv
from datetime import datetime
import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "--delay", type=int, default=2, help="Délai entre mesures (secondes)"
)
parser.add_argument(
    "--outfile", type=str, default="data/capteur_data.csv", help="Fichier CSV de sortie"
)
args = parser.parse_args()

# Ouvrir un fichier CSV en écriture
with open(args.outfile, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "humidite"])  # en-têtes du CSV

    while True:
        temperature = round(random.uniform(18, 30), 2)
        humidite = round(random.uniform(40, 80), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"{timestamp} | Température: {temperature}°C | Humidité: {humidite}%")
        writer.writerow([timestamp, temperature, humidite])
        file.flush()

        time.sleep(args.delay)
