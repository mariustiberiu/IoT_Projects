# 01_Graphiques_temps_reel

Ce module permet de visualiser en **temps réel** les données de température et d’humidité issues d’un fichier CSV (`sample.csv`).  
Il simule également des capteurs avec ajout automatique de nouvelles données toutes les 2 secondes et exporte les données mises à jour dans le dossier `exports/`.

---

## Fonctionnalités

- Lecture automatique des données depuis `data/sample.csv`.
- Graphique en **temps réel** avec Matplotlib (Température et Humidité).
- **Export automatique** des données dans `exports/`.
- Simulation de capteur ajoutant de nouvelles données toutes les 2 secondes.

---

## Structure des dossiers

01_Graphiques_temps_reel/
├─ data/
│ └─ sample.csv
├─ exports/
├─ screenshots/
│ ├─ screenshot_launch_terminal.png
│ ├─ screenshot_graph_initial.png
│ ├─ screenshot_graph_live.png
│ └─ screenshot_export_files.png
└─ src/
└─ main.py

yaml
Copier le code

---

## Exécution

1. Assurez-vous d’avoir Python et les bibliothèques nécessaires installées (`pandas`, `matplotlib`).  
2. Exécutez le script depuis le terminal :

```bash
cd Ch3_Dashboards_Visualisation/01_Graphiques_temps_reel/src
python main.py
Le graphique se met à jour automatiquement toutes les 2 secondes et les exports CSV sont créés dans exports/.

Captures d’écran
1. Lancement du script

Affichage du terminal au lancement du script python main.py. Montre que le script démarre et lit le CSV.

2. Graphique initial

Graphique initial juste après ouverture. Montre les premières courbes Température et Humidité.

3. Graphique en temps réel

Graphique en temps réel après quelques mises à jour. Illustre l’évolution des données et l’animation.

4. Fichiers exportés

Contenu du dossier exports/. Montre les fichiers CSV générés automatiquement à chaque mise à jour.

Remarques
Les données sont simulées pour l’instant ; il est possible de les remplacer par des capteurs réels.

Les fichiers CSV dans exports/ permettent de sauvegarder chaque état du graphique pour analyses futures.