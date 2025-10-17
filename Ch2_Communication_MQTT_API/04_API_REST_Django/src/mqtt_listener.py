import paho.mqtt.client as mqtt
import requests
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/#"
API_URL = "http://127.0.0.1:8000/api/data/"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connecté au broker MQTT ({BROKER}:{PORT})")
        client.subscribe(TOPIC)
        print(f"📡 Abonné au topic: {TOPIC}")
    else:
        print(f"❌ Échec de connexion MQTT. Code: {rc}")

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"📥 Reçu MQTT brut: {payload}")

        # Conversion en float si possible
        try:
            value = float(payload)
        except ValueError:
            value = payload

        data = {"topic": msg.topic, "value": value}
        print(f"📥 Reçu MQTT: {data}")

        # Envoi à l’API Django
        r = requests.post(API_URL, json=data)
        print(f"✅ POST API status: {r.status_code} - {r.text}")

    except Exception as e:
        print(f"❌ Erreur dans on_message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
print("🚀 Listener MQTT démarré...")

client.loop_forever()
