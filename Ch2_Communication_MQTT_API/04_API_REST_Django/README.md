Ch2_04 – API REST Django (Final)
Description

Ce projet met en place une API REST avec Django pour gérer les capteurs et les messages MQTT. L’API permet :

De recevoir et stocker des données de capteurs via MQTT

De fournir des endpoints REST pour consulter ou créer des messages

D’exporter automatiquement les données en CSV et JSON

De tester rapidement les publications via MQTT ou l’API REST

Cette version s’inspire des projets précédents (Ch2_01 à Ch2_03), mais apporte :

Intégration complète avec Django REST Framework

Gestion automatique des messages via /api/data/

Support pour l’export CSV/JSON similaire aux chapitres précédents

Installation

Créer et activer un environnement virtuel :

python -m venv .venv
.\.venv\Scripts\activate


Installer les dépendances :

pip install -r requirements.txt


requirements.txt contient :

django
djangorestframework
paho-mqtt
tabulate


Créer la base de données et appliquer les migrations :

python manage.py makemigrations
python manage.py migrate


Lancer le serveur Django :

python manage.py runserver

Structure du projet
04_API_REST_Django/
├─ README.md
├─ api_rest/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ backup/
├─ data/
│  ├─ sample.csv
│  └─ sample.json
├─ db.sqlite3
├─ exports/
│  ├─ mqtt_api_data.csv
│  └─ mqtt_api_data.json
├─ manage.py
├─ requirements.txt
├─ screenshots/
│  ├─ api_terminal_start.png
│  ├─ api_message_post.png
│  ├─ api_message_received.png
│  ├─ api_export_files.png
│  └─ api_quit_server.png
├─ sensors_api/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations/
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
└─ src/
   ├─ check_exports.py
   ├─ main.py
   ├─ mqtt_listener.py
   └─ mqtt_publisher.py

Endpoints REST

Lister toutes les données :

GET http://127.0.0.1:8000/api/data/


Ajouter une nouvelle donnée :

POST http://127.0.0.1:8000/api/data/
Content-Type: application/json

{
  "topic": "sensors/temperature",
  "value": 26.4
}

Publication via MQTT

Exemple depuis le script mqtt_publisher.py :

publish.single("sensors/temperature", "25.8", hostname="localhost")


Le listener (mqtt_listener.py) reçoit automatiquement les messages et les poste vers l’API REST.

Vérification des exports CSV/JSON

Script : src/check_exports.py

Résultat attendu : le fichier mqtt_api_data.csv et mqtt_api_data.json contiennent toutes les valeurs reçues via MQTT et API REST.

Commandes utiles

Lancer le serveur :

python src/manage.py runserver


Tester l’API avec curl :

curl -X POST http://127.0.0.1:8000/api/data/ -H "Content-Type: application/json" -d '{"topic":"sensors/temperature","value":24.5}'
curl http://127.0.0.1:8000/api/data/


Publier un message MQTT :

python src/mqtt_publisher.py

Screenshots recommandés
#	Nom du screenshot	Contexte / Où le capturer
1	api_terminal_start.png	Terminal principal : lancement serveur Django
2	api_message_post.png	Envoi d’un POST via Postman, Thunder Client ou curl
3	api_message_received.png	Message reçu via MQTT ou via API REST
4	api_export_files.png	Explorateur / VSCode : fichiers CSV/JSON générés dans exports/
5	api_quit_server.png	Terminal principal : arrêt du serveur Django
Notes

Les fichiers CSV/JSON sont générés automatiquement lors de la réception de messages via MQTT ou via l’API REST.

Les dossiers data et backup sont optionnels et peuvent servir à stocker des exemples ou sauvegardes.


Parfait, avec ces 5 screenshots, tu as quasiment tout ce qu’il faut pour documenter ton projet. Voici un petit check rapide :

api_terminal_start.png ✅

Montre le lancement du serveur Django.

Indispensable pour prouver que le serveur est opérationnel.

api_message_post.png ✅

Montre l’envoi d’un POST via Postman, Thunder Client ou curl.

Confirme que l’API reçoit les données.

api_message_received.png ✅

Montre la réception des données via MQTT et l’API REST.

Très important pour démontrer l’intégration MQTT → API REST.

api_export_files.png ✅

Montre les fichiers CSV/JSON générés dans exports/.

Vérifie que les données sont bien sauvegardées.

api_quit_server.png ✅

Montre l’arrêt propre du serveur Django.

Utile pour montrer la fermeture du serveur sans erreurs.

💡 Conclusion : Ces 5 screenshots couvrent tous les points essentiels : lancement du serveur, envoi de données, réception via MQTT, export, et arrêt du serveur. Tu n’as pas besoin d’en rajouter pour le README final.

Si tu veux, je peux te préparer un petit paragraphe final “Validation du projet” à ajouter à ton README pour rendre le tout encore plus pro et lisible. Veux‑tu que je fasse ça ?






















# Ch2_04 – API REST Django

## Description

Ce projet met en place une **API REST avec Django** pour gérer les capteurs et les messages MQTT. L’API permet de :

- Recevoir et stocker des données de capteurs via MQTT
- Fournir des endpoints REST pour consulter ou créer des messages
- Exporter les données en CSV et JSON
- Tester rapidement les publications avec MQTT ou l’interface REST

Cette version s’inspire des projets précédents Ch2_01 à Ch2_03, mais apporte :

- Intégration d’une API REST avec Django
- Gestion automatique des messages via les endpoints `/api/messages/`
- Possibilité d’envoyer des messages depuis un terminal ou un script Python
- Support pour l’export CSV/JSON similaire aux chapitres précédents

---

## Installation

1. Crée un environnement virtuel et active-le :

```powershell
python -m venv .venv
.\.venv\Scripts\activate

2 Installe les dépendances :
pip install -r requirements.txt

Django==4.3.0
djangorestframework==3.20.0
paho-mqtt==2.1.0

3 Crée la base de données Django et les migrations :
django-admin startproject api_rest .
python manage.py makemigrations
python manage.py migrate


4 Lance le serveur Django :

python manage.py runserver

5 Structure du projet
Ch2_Communication_MQTT_API
│
├─ 04_API_REST_Django
│  ├─ README.md
│  ├─ backup
│  ├─ data
│  │  ├─ sample.csv
│  │  └─ sample.json
│  ├─ exports
│  ├─ screenshots
│  │  ├─ api_terminal_start.png
│  │  ├─ api_message_post.png
│  │  ├─ api_message_received.png
│  │  ├─ api_export_files.png
│  │  └─ api_quit_server.png
│  └─ src
│     ├─ manage.py
│     ├─ mqtt_app
│     │  ├─ __init__.py
│     │  ├─ admin.py
│     │  ├─ apps.py
│     │  ├─ models.py
│     │  ├─ serializers.py
│     │  ├─ urls.py
│     │  └─ views.py
│     └─ mqtt_project
│        ├─ __init__.py
│        ├─ settings.py
│        ├─ urls.py
│        └─ wsgi.py


Commandes utiles

Lancer le serveur Django :

python src/manage.py runserver


Tester les endpoints REST :

# Exemple pour créer un message
curl -X POST http://127.0.0.1:8000/api/messages/ -H "Content-Type: application/json" -d '{"topic":"sensors/temperature","payload":"24.5"}'

# Exemple pour lister tous les messages
curl http://127.0.0.1:8000/api/messages/


Publier un message via MQTT (pour tester l’intégration) :

"C:\Program Files\mosquitto\mosquitto_pub.exe" -h localhost -t sensors/temperature -m "23.7"

Screenshots recommandés
#	Nom du screenshot	Où le capturer / Contexte
1	api_terminal_start.png	Terminal principal : lancement du serveur Django
2	api_message_post.png	Envoi d’un POST via curl ou Postman
3	api_message_received.png	Message reçu via MQTT ou via API
4	api_export_files.png	Explorateur / VSCode : fichiers CSV/JSON dans ../exports/
5	api_quit_server.png	Terminal principal : arrêt du serveur Django


Notes

Les fichiers CSV/JSON sont générés automatiquement lors de la réception de messages via MQTT ou l’API REST.

Les dossiers data et backup sont optionnels, ils peuvent servir à stocker des exemples ou sauvegardes.

Le projet utilise Django + DRF pour fournir une API REST simple et rapide à tester.


🧠 Ensuite :

1 On va déclarer l’application dans api_rest/settings.py.

2 Puis créer le modèle SensorData (pour stocker les données MQTT).

3 Et enfin exposer ça en API REST avec Django REST Framework.

🔧 Tests de l’API REST avec Postman ou Thunder Client
1️⃣ Lancer le serveur Django
python manage.py runserver


Le serveur écoute sur :

http://127.0.0.1:8000/

2️⃣ Tester avec Postman

Ouvre Postman

Clique sur “New Request”

Mets l’URL suivante :

http://127.0.0.1:8000/api/data/


Sélectionne POST

Dans l’onglet Body → raw → JSON, entre :

{
  "topic": "sensors/temperature",
  "value": 25.8
}


Clique sur Send ✅
→ Tu devrais recevoir une réponse 201 (Created) avec les données enregistrées.

Pour consulter les données :

Crée une requête GET sur la même URL :

http://127.0.0.1:8000/api/data/


Tu verras la liste JSON de toutes les mesures stockées.

3️⃣ Tester avec Thunder Client (extension VS Code)

Installe Thunder Client dans VS Code :

Ouvre la barre latérale à gauche → onglet “Extensions”

Recherche Thunder Client

Clique sur Installer

Ouvre Thunder Client (icône ⚡ dans la barre latérale)

Crée une nouvelle requête :

Méthode : POST

URL : http://127.0.0.1:8000/api/data/

Onglet Body → JSON :

{
  "topic": "sensors/humidity",
  "value": 45.3
}


Clique sur Send → tu verras la réponse JSON enregistrée.

Pour tester la lecture :

Change la méthode en GET

Garde la même URL : http://127.0.0.1:8000/api/data/

Clique sur Send pour voir toutes les entrées.