🧠 Ch2_03 – Interface Graphique MQTT (Tkinter)
🎯 Description

Ce projet introduit une interface graphique pour interagir avec un broker MQTT, permettant à l’utilisateur de :

Se connecter à un broker MQTT (par défaut : localhost:1883)

S’abonner à un topic (ex. sensors/#)

Visualiser en temps réel les messages reçus dans une fenêtre Tkinter

Publier manuellement des messages MQTT

Exporter les messages reçus en CSV et JSON

Quitter proprement via un bouton

Cette version s’inspire de Ch2_02, mais ajoute :

Une interface Tkinter intuitive

Des boutons pour Connecter, Publier, Exporter, Quitter

Des threads séparés pour ne pas bloquer la fenêtre

Une compatibilité totale avec les fichiers exportés des chapitres précédents

⚙️ Installation

Crée un environnement virtuel et active-le :

python -m venv .venv
.\.venv\Scripts\activate


Installe les dépendances :

pip install -r requirements.txt


requirements.txt

paho-mqtt
tk

🗂️ Structure du projet
Ch2_Communication_MQTT_API
│
├─ 03_Interface_graphique_MQTT
│  ├─ README.md
│  ├─ backup
│  ├─ data
│  │  ├─ sample.csv
│  │  └─ sample.json
│  ├─ exports
│  ├─ screenshots
│  │  ├─ gui_start.png
│  │  ├─ gui_connected.png
│  │  ├─ gui_message_received.png
│  │  ├─ gui_publish_message.png
│  │  ├─ gui_export_done.png
│  │  └─ gui_quit.png
│  └─ src
│     └─ main.py

▶️ Exécution
Lancer le programme
python src\main.py


La fenêtre graphique s’ouvre !

Cliquez sur Connecter pour démarrer la connexion au broker MQTT.

Une fois connecté, les messages reçus s’affichent dans la zone centrale.

Publier un message

Entrez un topic (par exemple sensors/manual)

Entrez un message (par exemple 28.5)

Cliquez sur Publier

Le message sera envoyé et affiché dans la fenêtre (📤 Message publié …).

Exporter les messages

Cliquez sur Exporter pour sauvegarder les messages reçus dans ../exports/mqtt_gui_data.csv et ../exports/mqtt_gui_data.json.

Si aucun message n’a encore été reçu, un message d’avertissement s’affiche.

Quitter le programme

Cliquez sur Quitter ou fermez la fenêtre Tkinter.

🧪 Test MQTT externe

Pour tester la réception des messages avec un client externe :

"C:\Program Files\mosquitto\mosquitto_pub.exe" -h localhost -t sensors/temperature -m "23.7" ou

& "C:\Program Files\mosquitto\mosquitto_pub.exe" -h localhost -t sensors/temperature -m "23.7"



Le message doit apparaître instantanément dans la fenêtre Tkinter (📥 sensors/temperature : 23.7).


#	Nom du screenshot	Où le capturer / Contexte
1	gui_start.png	Au lancement du programme, fenêtre Tkinter vide.
2	gui_connected.png	Après avoir cliqué sur Connecter (message ✅ Connecté au broker MQTT).
3	gui_message_received.png	Lorsqu’un message MQTT est reçu et affiché.
4	gui_publish_message.png	Après avoir envoyé un message depuis l’interface (📤 Message publié…).
5	gui_export_done.png	Après avoir cliqué sur Exporter (💾 Export terminé).
6	gui_quit.png	Fenêtre en train de se fermer ou message de fin.



L’interface Tkinter fonctionne, permet de se connecter au broker, publier des messages, et voir les logs.

Les exports CSV/JSON sont correctement générés dans ../exports lorsque des messages sont reçus.

Les warnings de Paho MQTT sont visibles mais le script reste fonctionnel.

Les dossiers data et backup ne sont pas nécessaires pour le fonctionnement actuel, mais je les conserve pour stocker des exemples ou historiques.

