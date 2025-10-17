03_Dashboard_Django_MongoDB/README.md)


Parfait, je vais te guider pour tes screenshots étape par étape pour que ça corresponde bien à ce que tu veux montrer dans ton projet. Je note aussi quelques précisions pour que les capteurs/export soient visibles correctement.

1️⃣ dashboard_complet.png

Objectif : Vue globale du dashboard avec les graphiques et les deux tableaux.

Comment faire :

Va sur http://127.0.0.1:8000/.

Vérifie que les graphiques Température et Humidité s’affichent.

Vérifie que le tableau des dernières lectures est rempli et que le tableau complet MongoDB est visible.

Fait une capture de l’écran entier (Ctrl+PrtSc ou Snipping Tool).

2️⃣ filtre_capteur.png

Objectif : Montrer le filtre en action.

Comment faire :

Dans le filtre “Filtrer par capteur”, sélectionne un capteur spécifique (ex : Capteur1).

Vérifie que le tableau Dernières lectures ne montre que ce capteur.

Capture cette vue.

3️⃣ tableau_mongodb.png

Objectif : Vue de toutes les données présentes dans MongoDB.

Comment faire :

Descends au tableau full-mongo-table (tableau complet MongoDB).

Vérifie que toutes les données sont listées.

Capture le tableau.

4️⃣ console_json.png

Objectif : Montrer la réponse JSON de ton API dernieres_lectures_api.

Comment faire :

Ouvre Outils développeur (F12) → onglet Network.

Recharge la page et sélectionne la requête vers dernieres_lectures_api.

Va dans l’onglet Response pour voir le JSON.

Capture la fenêtre avec le JSON visible.

5️⃣ export_csv.png

Objectif : Montrer que le bouton CSV fonctionne.

Comment faire :

Clique sur le bouton Exporter les données CSV.

Vérifie que le fichier est téléchargé dans ton dossier export ou via le navigateur (selon ton choix).

Capture l’écran montrant le téléchargement ou le fichier CSV ouvert.

6️⃣ export_json.png

Objectif : Montrer que le bouton JSON fonctionne.

Comment faire :

Clique sur le bouton Exporter en JSON.

Vérifie que le fichier JSON est bien généré dans le dossier export.

Capture l’écran montrant le fichier JSON ouvert ou la notification de succès.

💡 Conseil :
Pour les captures CSV/JSON, si tu veux que le capteur sélectionné soit visible dans l’export, fais d’abord le filtre sur le tableau avant de cliquer sur le bouton d’export. Ainsi, ton export correspondra exactement aux données filtrées.


📊 Visualisation temps réel avec Plotly
🧾 Tableau dynamique avec filtre par capteur
🌐 API pour les dernières lectures
🧠 Intégration Django ↔ MongoDB
📤 Export CSV — pour que l’utilisateur puisse télécharger les données affichées.
📤 Export Excel (facultatif mais pro).
🧹 Filtrer les données avant export (par capteur ou date).
🧰 Bouton dans le dashboard pour lancer l’export.

# Projet IoT - Dashboard Django + MongoDB (Ch03)









Dashboard Django affichant des lectures de capteurs stockées dans MongoDB (via MongoEngine).

📌 Description

Ce projet présente un dashboard IoT développé avec Django et connecté à MongoDB.
Il permet de :

Visualiser en temps réel les données de capteurs (température et humidité) avec Plotly

Filtrer par capteur les dernières lectures

Consulter toutes les données stockées dans MongoDB

Exporter les données CSV et JSON filtrées ou complètes

🛠 Fonctionnalités

Dashboard complet

Graphiques Température et Humidité

Tableau des dernières lectures (10 dernières)

Tableau complet MongoDB

Filtrage par capteur

Menu déroulant pour choisir un capteur spécifique

Tableau des dernières lectures mis à jour automatiquement

Export des données

CSV : téléchargement direct, filtrable par capteur

JSON : fichier généré dans le dossier export/, filtrable par capteur

Noms de fichiers générés automatiquement :

CSV → capteurs_YYYYMMDD_HHMMSS.csv

JSON → capteurs_YYYYMMDD_HHMMSS.json

Rafraîchissement automatique

Tableau des dernières lectures mis à jour toutes les 5 secondes via l’API dernieres_lectures_api

⚙️ Prérequis

Python 3.8+

MongoDB local ou distant

Virtualenv activé

🚀 Installation & Lancement

Activer l’environnement virtuel :

source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate      # Linux/Mac


Installer les dépendances :

pip install -r requirements.txt


Lancer MongoDB (exemple avec Docker) :

docker run -d -p 27017:27017 --name mongo mongo:6.0


Peupler la base de données (optionnel) :

python scripts/seed_from_csv.py ../data/sample.csv


Démarrer le serveur Django :

python manage.py runserver


Accéder au dashboard :

http://127.0.0.1:8000/


Simulateur (optionnel) :
Pour générer des lectures en continu :

python scripts/simulate_writer.py

🖼️ Screenshots à réaliser
Nom fichier	Contenu à capturer
dashboard_complet.png	Vue globale du dashboard (graphiques + tableau dernières lectures + tableau complet MongoDB)
filtre_capteur.png	Filtre activé sur un capteur spécifique, tableau dernières lectures filtré
tableau_mongodb.png	Tableau complet MongoDB (toutes les données visibles)
console_json.png	Réponse JSON dans Network/Console du navigateur
export_csv.png	Export CSV réussi (message ou fichier téléchargé dans export/)
export_json.png	Export JSON réussi (message ou fichier généré dans export/)

💡 Astuce : Pour les exports, sélectionne un capteur spécifique avant d’exporter pour montrer que le filtrage fonctionne.

📂 Structure du projet
03_Dashboard_Django_MongoDB/
├─ README.md
├─ backup/
├─ data/
│  ├─ sample.csv
│  └─ sample.json
├─ exports/                  # Fichiers export CSV/JSON générés
├─ requirements.txt
├─ screenshots/              # Screenshots finaux
│  ├─ console_json.png
│  ├─ dashboard_complet.png
│  ├─ filtre_capteur.png
│  └─ tableau_mongodb.png
├─ src/
│  ├─ dashboard/             # App Django
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations/
│  │  │  └─ __init__.py
│  │  ├─ models.py           # Modèles MongoEngine
│  │  ├─ mongo_connection.py # Connexion MongoDB
│  │  ├─ templates/dashboard/dashboard.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py            # Toutes les fonctions Dashboard + API + Export CSV/JSON
│  ├─ scripts/
│  │  ├─ seed_from_csv.py
│  │  └─ simulate_writer.py
│  ├─ manage.py
│  └─ project/
│     ├─ __init__.py
│     ├─ settings.py
│     ├─ urls.py
│     └─ wsgi.py

✅ Checklist pour finaliser le projet

Vérifier que les dernières lectures en temps réel fonctionnent bien avec toutes les données.

Vérifier que le tableau complet MongoDB affiche toutes les entrées.

Vérifier que le filtre par capteur fonctionne correctement.

Vérifier que les graphiques Température et Humidité s’affichent correctement.

Vérifier que l’export CSV et JSON fonctionne (filtrage par capteur possible).

Nettoyer tous les imports et codes inutiles dans views.py et mongo_connection.py.

⚡ Résumé des fonctionnalités

📊 Dashboard opérationnel avec les graphiques Température et Humidité ✔️

🧾 Tableau complet MongoDB fonctionnel ✔️

🔄 Filtre par capteur opérationnel ✔️

🧹 Code nettoyé dans views.py et mongo_connection.py ✔️

🖼️ README prêt avec noms des captures d’écran à fournir ✔️

🧠 Vérification API JSON depuis la console ✔️

Dashboard Django affichant des lectures de capteurs stockées dans MongoDB (via MongoEngine).

📌 Description

Ce projet présente un dashboard IoT développé avec Django et connecté à MongoDB.
Il permet de :

Visualiser en temps réel les données de capteurs (température et humidité) avec Plotly

Filtrer par capteur les dernières lectures

Consulter toutes les données stockées dans MongoDB

Exporter les données CSV et JSON filtrées ou complètes

🛠 Fonctionnalités

Dashboard complet

Graphiques Température et Humidité

Tableau des dernières lectures (10 dernières)

Tableau complet MongoDB

Filtrage par capteur

Menu déroulant pour choisir un capteur spécifique

Tableau des dernières lectures mis à jour automatiquement

Export des données

CSV : téléchargement direct, filtrable par capteur

JSON : fichier généré dans le dossier export/, filtrable par capteur

Noms de fichiers générés automatiquement :

CSV → capteurs_YYYYMMDD_HHMMSS.csv

JSON → capteurs_YYYYMMDD_HHMMSS.json

Rafraîchissement automatique

Tableau des dernières lectures mis à jour toutes les 5 secondes via l’API dernieres_lectures_api

⚙️ Prérequis

Python 3.8+

MongoDB local ou distant

Virtualenv activé

🚀 Installation & Lancement

Activer l’environnement virtuel :

source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate      # Linux/Mac


Installer les dépendances :

pip install -r requirements.txt


Lancer MongoDB (exemple avec Docker) :

docker run -d -p 27017:27017 --name mongo mongo:6.0


Peupler la base de données (optionnel) :

python scripts/seed_from_csv.py ../data/sample.csv


Démarrer le serveur Django :

python manage.py runserver


Accéder au dashboard :

http://127.0.0.1:8000/


Simulateur (optionnel) :
Pour générer des lectures en continu :

python scripts/simulate_writer.py

🖼️ Screenshots à réaliser
Nom fichier	Contenu à capturer
dashboard_complet.png	Vue globale du dashboard (graphiques + tableau dernières lectures + tableau complet MongoDB)
filtre_capteur.png	Filtre activé sur un capteur spécifique, tableau dernières lectures filtré
tableau_mongodb.png	Tableau complet MongoDB (toutes les données visibles)
console_json.png	Réponse JSON dans Network/Console du navigateur
export_csv.png	Export CSV réussi (message ou fichier téléchargé dans export/)
export_json.png	Export JSON réussi (message ou fichier généré dans export/)

💡 Astuce : Pour les exports, sélectionne un capteur spécifique avant d’exporter pour montrer que le filtrage fonctionne.

📂 Structure du projet
03_Dashboard_Django_MongoDB/
├─ README.md
├─ backup/
├─ data/
│  ├─ sample.csv
│  └─ sample.json
├─ exports/                  # Fichiers export CSV/JSON générés
├─ requirements.txt
├─ screenshots/              # Screenshots finaux
│  ├─ console_json.png
│  ├─ dashboard_complet.png
│  ├─ filtre_capteur.png
│  └─ tableau_mongodb.png
├─ src/
│  ├─ dashboard/             # App Django
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations/
│  │  │  └─ __init__.py
│  │  ├─ models.py           # Modèles MongoEngine
│  │  ├─ mongo_connection.py # Connexion MongoDB
│  │  ├─ templates/dashboard/dashboard.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py            # Toutes les fonctions Dashboard + API + Export CSV/JSON
│  ├─ scripts/
│  │  ├─ seed_from_csv.py
│  │  └─ simulate_writer.py
│  ├─ manage.py
│  └─ project/
│     ├─ __init__.py
│     ├─ settings.py
│     ├─ urls.py
│     └─ wsgi.py

✅ Checklist pour finaliser le projet

1 Vérifier que les dernières lectures en temps réel fonctionnent bien avec toutes les données.

2 Vérifier que le tableau complet MongoDB affiche toutes les entrées.

3 Vérifier que le filtre par capteur fonctionne correctement.

4 Vérifier que les graphiques Température et Humidité s’affichent correctement.

5 Vérifier que l’export CSV et JSON fonctionne (filtrage par capteur possible).

6 Nettoyer tous les imports et codes inutiles dans views.py et mongo_connection.py.

⚡ Résumé des fonctionnalités
📊 Dashboard opérationnel avec les graphiques Température et Humidité ✔️
🧾 Tableau complet MongoDB fonctionnel ✔️
🔄 Filtre par capteur opérationnel ✔️
🧹 Code nettoyé dans views.py et mongo_connection.py ✔️
🖼️ README prêt avec noms des captures d’écran à fournir ✔️
🧠 Vérification API JSON depuis la console ✔️