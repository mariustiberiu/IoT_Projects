import paho.mqtt.publish as publish
import requests
import csv, json, os
from datetime import datetime
import random
import time

# --- Config ---
BROKER = "localhost"  # ou "test.mosquitto.org"
PORT = 1883
TOPIC = "sensors/temperature"

API_URL = "http://127.0.0.1:8000/api/data/"

OUTPUT_CSV = "../exports/mqtt_api_data.csv"
OUTPUT_JSON = "../exports/mqtt_api_data.json"

os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

# --- Fonctions de sauvegarde ---
def save_to_csv(data):
    file_exists = os.path.isfile(OUTPUT_CSV)
    with open(OUTPUT_CSV, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "topic", "value"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def save_to_json(data):
    messages = []
    if os.path.isfile(OUTPUT_JSON):
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = []
    messages.append(data)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)

# --- Boucle de publication ---
for i in range(10):  # publier 10 messages
    value = round(random.uniform(25.0, 27.0), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"timestamp": timestamp, "topic": TOPIC, "value": value}

    # Publier sur MQTT
    try:
        publish.single(TOPIC, str(value), hostname=BROKER, port=PORT)
        print(f"✅ Message MQTT envoyé → Topic: {TOPIC}, Valeur: {value}")
    except Exception as e:
        print(f"❌ Erreur MQTT : {e}")

    # Sauvegarder CSV/JSON
    save_to_csv(data)
    save_to_json(data)

    # Envoyer au API REST Django
    try:
        resp = requests.post(API_URL, json={"topic": TOPIC, "value": value})
        if resp.status_code == 201:
            print(f"✅ POST API status: {resp.status_code} - {resp.json()}")
        else:
            print(f"⚠️ POST API status: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"❌ Erreur API : {e}")

    time.sleep(2)  # délai entre chaque message
