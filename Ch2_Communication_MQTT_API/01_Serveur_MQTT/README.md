1. Description du projet

Ce projet met en place un serveur MQTT en Python qui :

Se connecte à un broker MQTT local (localhost) sur le port 1883.

Souscrit à des topics (sensors/#) pour recevoir des messages.

Enregistre les messages dans CSV et JSON (../exports/mqtt_data.csv et .json).

Peut simuler automatiquement plusieurs capteurs envoyant des messages toutes les quelques secondes.

Fonctionne en arrière-plan pour permettre l’utilisation du terminal pendant l’exécution.

2. Prérequis

Python 3.11+

paho-mqtt installé :

pip install paho-mqtt


Mosquitto installé et en service sur Windows.
Vérifier que Mosquitto fonctionne :

mosquitto -v
net start mosquitto

3. Structure du projet
01_Serveur_MQTT/
├─ src/
│  ├─ main.py          # script principal MQTT
├─ exports/
│  ├─ mqtt_data.csv
│  └─ mqtt_data.json

4. Exécution du programme
4.1 Exécution standard
python main.py


Connexion au broker.

Souscription au topic sensors/#.

Le terminal reste interactif pour taper q et quitter.

4.2 Exécution avec simulation
python main.py --simulate


Active l’envoi automatique de messages simulés par plusieurs capteurs.

Messages sauvegardés automatiquement en CSV et JSON.

4.3 Options CLI
Option	Description
--broker	Adresse du broker MQTT (par défaut : localhost)
--port	Port du broker MQTT (par défaut : 1883)
--topic	Topic à souscrire (par défaut : sensors/#)
--format	Format d’export : csv, json, both (par défaut : both)
--output	Chemin de base pour les fichiers export (sans extension, par défaut : ../exports/mqtt_data)
--simulate	Activer la simulation automatique de messages capteurs
5. Publication de messages externes

Dans un autre terminal, pour tester la réception :

"C:\Program Files\mosquitto\mosquitto_pub.exe" -h localhost -t sensors/temperature -m "23.7"


Le message sera reçu par le main.py et sauvegardé dans les fichiers export.

6. Sortie du programme

Pour quitter le programme, tape q dans le terminal principal :

Tapez 'q' pour quitter : q
👋 Fin du programme.