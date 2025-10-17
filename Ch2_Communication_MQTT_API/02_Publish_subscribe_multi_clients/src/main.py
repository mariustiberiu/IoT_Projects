# main.py pour 02_Publish_subscribe_multi_clients
import argparse, csv, json, os, threading, time, random
from datetime import datetime
import paho.mqtt.client as mqtt

# --- Fonctions utilitaires ---
def save_to_csv(data, output_path):
    file_exists = os.path.isfile(output_path)
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp","topic","payload"])
        if not file_exists: writer.writeheader()
        writer.writerow(data)

def save_to_json(data, output_path):
    messages = []
    if os.path.isfile(output_path):
        with open(output_path,"r",encoding="utf-8") as f:
            try: messages = json.load(f)
            except json.JSONDecodeError: messages=[]
    messages.append(data)
    with open(output_path,"w",encoding="utf-8") as f: json.dump(messages,f,indent=2)

# --- Callbacks MQTT ---
def on_connect(client, userdata, flags, rc):
    if rc==0: 
        print(f"✅ Connecté au broker MQTT {userdata['client_name']} avec code {rc}")
        client.subscribe(userdata['topic'])
        print(f"📡 {userdata['client_name']} souscrit au topic: {userdata['topic']}")
    else: print(f"❌ Échec de connexion {userdata['client_name']}, code {rc}")

def on_message(client, userdata, msg):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload=msg.payload.decode()
    data={"timestamp":timestamp,"topic":msg.topic,"payload":payload}
    print(f"📥 {userdata['client_name']} message reçu: {data}")
    if userdata['format'] in ("csv","both"): save_to_csv(data, userdata['output_csv'])
    if userdata['format'] in ("json","both"): save_to_json(data, userdata['output_json'])

# --- Simulation multi-clients ---
def simulate_sensors(client, stop_event):
    topics=["sensors/temperature","sensors/humidity"]
    while not stop_event.is_set():
        topic=random.choice(topics)
        payload=round(random.uniform(20,30),1) if "temperature" in topic else random.randint(30,80)
        client.publish(topic,payload)
        print(f"📤 Message simulé {client._client_id.decode()}: {topic}={payload}")
        time.sleep(5)

# --- Main ---
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--broker", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=1883)
    parser.add_argument("--topic", type=str, default="sensors/#")
    parser.add_argument("--format", type=str, choices=["csv","json","both"], default="both")
    parser.add_argument("--output", type=str, default="../exports/mqtt_data")
    parser.add_argument("--simulate", action="store_true")
    args=parser.parse_args()

    output_csv=args.output+".csv"
    output_json=args.output+".json"

    # Création de plusieurs clients
    clients=[]
    stop_event=threading.Event()
    for i in range(2): # deux clients pour l'exemple
        userdata={"topic":args.topic,"output_csv":output_csv,"output_json":output_json,"format":args.format,"client_name":f"Client_{i+1}"}
        client=mqtt.Client(userdata=userdata, client_id=f"client_{i+1}")
        client.on_connect=on_connect
        client.on_message=on_message
        client.connect(args.broker,args.port,keepalive=60)
        t=threading.Thread(target=client.loop_forever)
        t.daemon=True
        t.start()
        clients.append((client,t))
    
    print("✅ Multi-clients MQTT en arrière-plan")
    
    if args.simulate:
        for client,_ in clients:
            t_sim=threading.Thread(target=simulate_sensors,args=(client,stop_event))
            t_sim.daemon=True
            t_sim.start()
        print("✅ Simulation multi-capteurs activée")

    while True:
        cmd=input("Tapez 'q' pour quitter : ").strip().lower()
        if cmd=="q":
            stop_event.set()
            print("👋 Fin du programme multi-clients.")
            break

if __name__=="__main__":
    main()



"""
=== Ch2_02 – Serveur MQTT avec simulation de capteurs ===

Différences principales par rapport à Ch2_01 :
1. Ajout de l’option '--simulate' pour générer automatiquement des messages de capteurs simulés.
2. Utilisation d’un thread séparé pour la simulation afin que le terminal reste interactif.
3. Export automatique des messages reçus en CSV et en JSON (comme dans Ch2_01).
4. Boucle interactive : possibilité de quitter proprement avec la touche 'q'.
5. Liste recommandée de captures d’écran pour la documentation :
   - mqtt_terminal_start.png
   - mqtt_connected.png
   - mqtt_subscribed.png
   - mqtt_message_received.png
   - mqtt_simulation_enabled.png
   - mqtt_simulated_message.png
   - mqtt_export_files.png
   - mqtt_quit_program.png
   - mqtt_pub_external.png
"""
