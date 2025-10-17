"""
Usage: python seed_from_csv.py path/to/sample.csv

Le CSV attendu : timestamp,temperature,humidity[,sensor_name]
timestamp format: YYYY-MM-DD HH:MM:SS or ISO
"""
import sys
import pandas as pd
import os
import django
# on doit s'assurer que Django settings sont accessibles
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from dashboard.models import SensorData
from datetime import datetime

def seed(csv_path):
    df = pd.read_csv(csv_path)
    # normalise colonnes
    if "sensor_name" not in df.columns:
        df["sensor_name"] = "sensor_1"
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    SensorData.objects.delete()  # optionnel: vide la collection avant seed
    for _, row in df.iterrows():
        SensorData(
            sensor_name=str(row["sensor_name"]),
            temperature=float(row["temperature"]),
            humidity=float(row["humidity"]),
            timestamp=row["timestamp"].to_pydatetime()
        ).save()
    print(f"Inserted {len(df)} documents into MongoDB.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seed_from_csv.py path/to/sample.csv")
        sys.exit(1)
    seed(sys.argv[1])

