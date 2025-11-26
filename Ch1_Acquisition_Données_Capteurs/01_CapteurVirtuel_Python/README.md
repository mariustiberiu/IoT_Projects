# Chapitre 1 – Capteur Virtuel en Python

## Description
Ce projet présente un **capteur virtuel simulé en Python**, utilisé pour générer des données de capteurs (par exemple température et humidité) afin de tester les étapes suivantes du traitement et de la visualisation des données. 

Le capteur virtuel permet de :  
- Générer des messages simulés dans la console.  
- Tester la réception de données en temps réel.  
- Préparer les exports CSV/JSON et la visualisation graphique pour les chapitres suivants.

## Prérequis
- **Python 3.10+** installé.  
- Installer les dépendances (si nécessaire) :
```bash
pip install -r requirements.txt


## Captures d'écran
1. **Lancement du script** :  
   ![Lancement](screenshots/1screenshot_console_lancement.png)

2. **Message reçu du capteur** :  
   ![Message reçu](screenshots/2screenshot_console_message_recu.png)


Étapes d'utilisation

1 Cloner le projet ou naviguer dans le dossier 01_CapteurVirtuel_Python.
2 Activer l’environnement virtuel (si présent) :

python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux/Mac

3 Lancer le script principal (simulé ici avec le script console) :

python main.py