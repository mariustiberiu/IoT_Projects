import os

# Définition des chapitres et sous-parties
structure = {
    "Ch1_Acquisition_Donnees_Capteurs": {
        "01_CapteurVirtuel_Python": """# Simulation de capteur virtuel
import random, time

def main():
    while True:
        valeur = random.uniform(20, 30)
        print(f"🌡️ Température simulée : {valeur:.2f} °C")
        time.sleep(2)

if __name__ == "__main__":
    main()
""",
        "02_LectureSerie_PySerial": """# Lecture de données série avec pyserial
import serial

ser = serial.Serial('COM3', 9600)
while True:
    data = ser.readline().decode().strip()
    print(f"📡 Donnée reçue : {data}")
"""
    },

    "Ch2_Communication_IoT": {
        "01_MQTT_Base": """# Exemple MQTT
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "iot/test"

def on_message(client, userdata, msg):
    print(f"📩 {msg.payload.decode()} sur {msg.topic}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
print("📡 Client MQTT démarré...")
client.loop_forever()
""",
        "02_HTTP_Requetes": """# Exemple HTTP GET avec requests
import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
resp = requests.get(url)
print("🌍 Données reçues:", resp.json())
"""
    },

    "Ch3_Analyse_Visualisation": {
        "01_AnalyseCSV_Pandas": """# Analyse CSV avec pandas
import pandas as pd

df = pd.read_csv("../data/donnees.csv")
print("📊 Aperçu des données :")
print(df.head())
""",
        "02_Visualisation_Matplotlib": """# Visualisation matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [i**2 for i in x]
plt.plot(x, y, marker="o")
plt.title("📈 Exemple: y = x^2")
plt.show()
"""
    },

    "Ch4_Securite_IoT": {
        "01_Chiffrement_RSA": """# Exemple RSA avec cryptography
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
print("🔑 Clé privée générée :", key)
""",
        "02_Authentification_Token": """# Exemple token avec secrets
import secrets
token = secrets.token_hex(16)
print("🔐 Token généré:", token)
"""
    },

    "Ch5_Integration_Systemes": {
        "01_API_Flask": """# API REST simple avec Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "👋 Hello IoT API"

app.run(port=5000)
""",
        "02_Monitoring_Systeme": """# Monitoring système avec psutil
import psutil

print("💻 CPU %:", psutil.cpu_percent())
print("🧠 Mémoire %:", psutil.virtual_memory().percent)
"""
    },

    "Ch6_Cloud_Edge_Computing": {
        "01_Cloud_AWS_IoT": """# Connexion Cloud AWS IoT (placeholder)
print("☁️ Simulation de connexion AWS IoT Core")
""",
        "02_Edge_RaspberryPi": """# Edge Computing Raspberry Pi (simulation)
import time
while True:
    print("🍓 Traitement Edge en cours...")
    time.sleep(3)
"""
    }
}

for chapter, topics in structure.items():
    for topic, code in topics.items():
        base_path = os.path.join(chapter, topic)
        src_path = os.path.join(base_path, "src")
        data_path = os.path.join(base_path, "data")
        screenshots_path = os.path.join(base_path, "screenshots")

        os.makedirs(src_path, exist_ok=True)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(screenshots_path, exist_ok=True)

        # README
        readme_file = os.path.join(base_path, "README.md")
        with open(readme_file, "w", encoding="utf-8") as f:
            f.write(f"# {topic}\n\nProjet du chapitre {chapter}\n")

        # Script spécifique
        script_file = os.path.join(src_path, f"{topic.lower()}.py")
        with open(script_file, "w", encoding="utf-8") as f:
            f.write(code)

        # Screenshot placeholder
        screenshot_file = os.path.join(screenshots_path, f"screenshot_console_{topic}.png")
        with open(screenshot_file, "wb") as f:
            pass

print("✅ Tous les chapitres et scripts spécifiques ont été générés !")
