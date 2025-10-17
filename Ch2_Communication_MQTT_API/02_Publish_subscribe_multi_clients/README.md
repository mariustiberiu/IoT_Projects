# Ch2_02 – Publish / Subscribe Multi-Clients MQTT

## Description

Ce projet met en place un **serveur MQTT** capable de :

- Souscrire à des topics MQTT (par défaut `sensors/#`)
- Recevoir et afficher les messages en temps réel
- Exporter automatiquement les données dans **CSV** et **JSON**
- Simuler des capteurs pour envoyer des messages automatiques
- Rester interactif dans le terminal avec possibilité de quitter proprement (`q`)

Cette version s’inspire du Ch2_01, mais ajoute :

- Simulation automatique de capteurs avec `--simulate`
- Threads séparés pour MQTT et simulation afin de ne pas bloquer le terminal
- Export simultané en CSV et JSON
- Gestion facile pour tester avec `mosquitto_pub.exe` depuis un autre terminal

---

## Installation

1. Crée un environnement virtuel et active-le :

```powershell
python -m venv .venv
.\.venv\Scripts\activate


Installer les dépendances :

pip install -r requirements.txt


requirements.txt doit contenir :

paho-mqtt

Structure du projet
Ch2_Communication_MQTT_API
│
├─ 02_Publish_subscribe_multi_clients
│  ├─ README.md
│  ├─ backup
│  ├─ data
│  │  ├─ sample.csv
│  │  └─ sample.json
│  ├─ exports
│  ├─ screenshots
│  │  ├─ mqtt_terminal_start.png
│  │  ├─ mqtt_connected.png
│  │  ├─ mqtt_subscribed.png
│  │  ├─ mqtt_message_received.png
│  │  ├─ mqtt_simulation_enabled.png
│  │  ├─ mqtt_simulated_message.png
│  │  ├─ mqtt_export_files.png
│  │  ├─ mqtt_quit_program.png
│  │  └─ mqtt_pub_external.png
│  └─ src
│     └─ main.py

Commandes CLI

Exemple de commandes pour exécuter le programme :

# Lancer le serveur MQTT et écouter les topics
python src\main.py

# Lancer le serveur et activer la simulation de capteurs
python src\main.py --simulate

# Spécifier un broker et un port personnalisés
python src\main.py --broker localhost --port 1883 --topic "sensors/#" --format both --output ../exports/mqtt_data


Pendant l’exécution, le terminal reste interactif. Tapez q pour quitter le programme proprement.

Tests avec mosquitto_pub.exe

Ouvrir un autre terminal et envoyer un message :

"C:\Program Files\mosquitto\mosquitto_pub.exe" -h localhost -t sensors/temperature -m "23.7"


Le message doit apparaître dans le terminal principal et être enregistré dans ../exports/mqtt_data.csv et ../exports/mqtt_data.json

Notes

Les exports CSV/JSON sont mis à jour à chaque message reçu.

La simulation de capteurs génère des messages toutes les 5 secondes par défaut.

Le programme est conçu pour rester interactif grâce à l’utilisation de threads pour MQTT et la simulation.

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
