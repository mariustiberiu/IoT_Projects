import argparse
import csv
import json
import os
import threading
import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

# --- Fonctions utilitaires ---

def save_to_csv(data, output_path):
    """Ajoute une ligne au fichier CSV"""
    file_exists = os.path.isfile(output_path)
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "topic", "payload"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def save_to_json(data, output_path):
    """Ajoute une ligne au fichier JSON (liste de messages)"""
    messages = []
    if os.path.isfile(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = []
    messages.append(data)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)

# --- Callbacks MQTT ---

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connecté au broker MQTT avec le code de résultat {rc}")
        client.subscribe(userdata['topic'])
        print(f"📡 Souscrit au topic : {userdata['topic']}")
    else:
        print(f"❌ Échec de connexion, code {rc}")

def on_message(client, userdata, msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = msg.payload.decode()
    data = {"timestamp": timestamp, "topic": msg.topic, "payload": payload}
    print(f"📥 Message reçu : {data}")
    
    if userdata['format'] in ("csv", "both"):
        save_to_csv(data, userdata['output_csv'])
    if userdata['format'] in ("json", "both"):
        save_to_json(data, userdata['output_json'])

# --- Simulation des capteurs ---

def simulate_sensors(client, stop_event):
    topics = ["sensors/temperature", "sensors/humidity"]
    while not stop_event.is_set():
        topic = random.choice(topics)
        payload = round(random.uniform(20, 30), 1) if "temperature" in topic else random.randint(30, 80)
        client.publish(topic, payload)
        print(f"📤 Message simulé envoyé : topic={topic}, payload={payload}")
        time.sleep(5)  # pause de 5 secondes

# --- Main ---

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--broker", type=str, default="localhost", help="Adresse du broker MQTT")
    parser.add_argument("--port", type=int, default=1883, help="Port du broker MQTT")
    parser.add_argument("--topic", type=str, default="sensors/#", help="Topic à souscrire")
    parser.add_argument("--format", type=str, choices=["csv", "json", "both"], default="both", help="Format d'export")
    parser.add_argument("--output", type=str, default="../exports/mqtt_data", help="Chemin du fichier export (sans extension)")
    parser.add_argument("--simulate", action="store_true", help="Activer la simulation automatique des capteurs")
    args = parser.parse_args()

    # Préparer les chemins
    output_csv = args.output + ".csv"
    output_json = args.output + ".json"

    userdata = {
        "topic": args.topic,
        "output_csv": output_csv,
        "output_json": output_json,
        "format": args.format
    }

    client = mqtt.Client(userdata=userdata)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(args.broker, args.port, keepalive=60)

    # --- Thread MQTT pour ne pas bloquer ---
    mqtt_thread = threading.Thread(target=client.loop_forever)
    mqtt_thread.daemon = True
    mqtt_thread.start()

    print("✅ MQTT en arrière-plan, vous pouvez continuer à utiliser le terminal.")

    # --- Thread simulation si activé ---
    stop_event = threading.Event()
    if args.simulate:
        sim_thread = threading.Thread(target=simulate_sensors, args=(client, stop_event))
        sim_thread.daemon = True
        sim_thread.start()
        print("✅ Simulation de capteurs en arrière-plan activée.")

    # --- Boucle interactive pour quitter ---
    while True:
        cmd = input("Tapez 'q' pour quitter : ").strip().lower()
        if cmd == "q":
            stop_event.set()
            print("👋 Fin du programme.")
            break

if __name__ == "__main__":
    main()

"""
============================================================
Serveur MQTT : Capture et export de données avec simulation
============================================================

Fonctionnalités principales :
1. Connexion à un broker MQTT (par défaut localhost:1883)
2. Souscription à un topic (par défaut "sensors/#")
3. Réception et affichage des messages MQTT en temps réel
4. Export automatique des messages reçus :
   - CSV : ../exports/mqtt_data.csv
   - JSON : ../exports/mqtt_data.json
5. Option de simulation (--simulate) :
   - Génère des messages aléatoires pour plusieurs capteurs
   - Température, humidité, ou autres topics définis
   - Envoie les messages à intervalles réguliers
6. Fonctionnement en arrière-plan grâce à un thread :
   - Le programme ne bloque pas le terminal
   - Permet de publier manuellement ou d'exécuter d'autres commandes
7. Interaction utilisateur :
   - Tapez 'q' pour quitter le programme proprement
8. Format d’export configurable via l’option --format :
   - csv : export CSV uniquement
   - json : export JSON uniquement
   - both : CSV + JSON (par défaut)

Exemples d'utilisation :

- Lancer le serveur MQTT avec export par défaut :
    python main.py

- Lancer le serveur MQTT avec simulation de capteurs :
    python main.py --simulate

- Lancer le serveur MQTT avec un topic personnalisé et export JSON uniquement :
    python main.py --topic "sensors/temperature" --format json --output ../exports/temperature_data

Notes :
- Les fichiers CSV et JSON sont créés automatiquement si inexistants.
- La simulation continue jusqu'à ce que l'utilisateur tape 'q'.
- Compatible avec tout broker MQTT local ou distant (configurable via --broker et --port).

============================================================
"""
