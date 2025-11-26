import tkinter as tk
from tkinter import scrolledtext, messagebox
import paho.mqtt.client as mqtt
import threading
import json, csv, os
from datetime import datetime

# --- Répertoires et fichiers ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPORT_DIR = os.path.join(BASE_DIR, "../exports")
os.makedirs(EXPORT_DIR, exist_ok=True)

CSV_FILE = os.path.join(EXPORT_DIR, "mqtt_gui_data.csv")
JSON_FILE = os.path.join(EXPORT_DIR, "mqtt_gui_data.json")

# --- Sauvegardes CSV/JSON ---
def save_to_csv(data, output_path=CSV_FILE):
    file_exists = os.path.isfile(output_path)
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "topic", "payload"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def save_to_json(data, output_path=JSON_FILE):
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
        userdata["log"]("✅ Connecté au broker MQTT\n")
        # Souscrire une seule fois
        if not getattr(client, "_subscribed", False):
            client.subscribe(userdata["topic"])
            client._subscribed = True
            userdata["log"](f"📡 Souscrit au topic : {userdata['topic']}\n")
    else:
        userdata["log"](f"❌ Erreur de connexion ({rc})\n")

def on_message(client, userdata, msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = msg.payload.decode()
    data = {"timestamp": timestamp, "topic": msg.topic, "payload": payload}
    userdata["log"](f"📥 {timestamp} - {msg.topic} : {payload}\n")
    if userdata["format"] in ("csv", "both"):
        save_to_csv(data, userdata["output_csv"])
    if userdata["format"] in ("json", "both"):
        save_to_json(data, userdata["output_json"])

# --- Interface Tkinter ---
class MQTTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ch2_03 - Interface MQTT")
        self.root.geometry("700x500")

        self.broker = "localhost"
        self.port = 1883
        self.topic = "sensors/#"
        self.format = "both"
        self.output_csv = CSV_FILE
        self.output_json = JSON_FILE
        self.client = None  # Pour vérifier la connexion

        # Zone d’affichage
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.text_area.pack(pady=10)

        # Zone d’envoi
        frame_send = tk.Frame(root)
        frame_send.pack(pady=5)
        tk.Label(frame_send, text="Topic :").grid(row=0, column=0)
        self.entry_topic = tk.Entry(frame_send, width=25)
        self.entry_topic.insert(0, "sensors/manual")
        self.entry_topic.grid(row=0, column=1, padx=5)
        tk.Label(frame_send, text="Message :").grid(row=0, column=2)
        self.entry_msg = tk.Entry(frame_send, width=25)
        self.entry_msg.grid(row=0, column=3, padx=5)

        # Boutons
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)
        self.btn_connect = tk.Button(frame_btn, text="Connecter", command=self.connect_mqtt)
        self.btn_connect.grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Publier", command=self.publish_message).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Exporter", command=self.export_files).grid(row=0, column=2, padx=5)
        tk.Button(frame_btn, text="Quitter", command=self.root.quit).grid(row=0, column=3, padx=5)

    def log(self, msg):
        self.text_area.insert(tk.END, msg)
        self.text_area.see(tk.END)

    def connect_mqtt(self):
        if self.client:
            self.log("⚠️ Déjà connecté au broker\n")
            return

        self.client = mqtt.Client(userdata={
            "topic": self.topic,
            "output_csv": self.output_csv,
            "output_json": self.output_json,
            "format": self.format,
            "log": self.log
        })
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect(self.broker, self.port, keepalive=60)
        
         # --- TLS/SSL ---
        self.client.tls_set(
            ca_certs="../docker/certs/ca.crt",
            certfile="../docker/certs/server.crt",
            keyfile="../docker/certs/server.key"
    )

        self.client.connect(self.broker, 8883, keepalive=60)  # Port TLS
        # Démarrage thread MQTT
        self.thread = threading.Thread(target=self.client.loop_forever, daemon=True)
        self.thread.start()
        self.log("🚀 Connexion en cours...\n")

        # Désactiver le bouton
        self.btn_connect.config(state="disabled")

    def publish_message(self):
        if not self.client:
            messagebox.showwarning("Pas connecté", "Connectez-vous au broker avant de publier.")
            return
        topic = self.entry_topic.get().strip()
        msg = self.entry_msg.get().strip()
        if topic and msg:
            self.client.publish(topic, msg)
            self.log(f"📤 Message publié : {topic} -> {msg}\n")
        else:
            messagebox.showwarning("Champs vides", "Veuillez entrer un topic et un message.")

    def export_files(self):
        csv_ok = os.path.exists(self.output_csv) and os.path.getsize(self.output_csv) > 0
        json_ok = os.path.exists(self.output_json) and os.path.getsize(self.output_json) > 0

        if csv_ok:
            self.log(f"💾 CSV présent : {os.path.abspath(self.output_csv)}\n")
        else:
            self.log("⚠️ CSV vide ou inexistant\n")
        if json_ok:
            self.log(f"💾 JSON présent : {os.path.abspath(self.output_json)}\n")
        else:
            self.log("⚠️ JSON vide ou inexistant\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = MQTTApp(root)
    root.mainloop()
