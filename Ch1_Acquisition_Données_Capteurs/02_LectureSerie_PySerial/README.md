# 02 - Lecture via port série (PySerial)

## 🎯 Objectif
Lire des mesures depuis un port série (Arduino/ESP) ou simuler des mesures localement.  
Enregistrer les valeurs dans `data/sample_from_serial.csv`.

---

## 🛠 Technologies
- Python 3.13
- pyserial (optionnel si vous utilisez un Arduino réel)

---

## 🔹 Fonctionnement

### Mode simulation
- Génère des mesures de température et humidité aléatoires.  
- Utile si vous n’avez pas de matériel Arduino.  
- Commande :  
```powershell
python src/lecture_serial.py --mode simulation --duree 10


Strucute

02_LectureSerie_PySerial/
      ├── .venv/                      # environnement virtuel local (NE PAS pousser sur GitHub)
      ├── src/
      │   └── lecture_serial.py       # script Python principal
      ├── arduino/
      │   └── capteur_simule.ino      # code Arduino optionnel
      ├── data/
      │   └── sample_from_serial.csv  # petit échantillon
      ├── screenshots/
      │   └── screenshot_console_serial_01.png
      ├── README.md                   # doc spécifique à 02
      ├── requirements.txt
      └── .gitignore





Mode Arduino

Lit les mesures envoyées par un Arduino branché sur un port série.

Avant de lancer, vérifier le port série réel via le Gestionnaire de périphériques (ex : COM4).

Commande :

python src/lecture_serial.py --mode arduino --port COM4 --duree 10


⚠️ Si aucun port n’est détecté, le script affiche un message clair et ne démarre pas.

🔹 Extrait Arduino (optionnel)

Si vous avez un Arduino ou ESP et voulez envoyer T:xx;H:yy via le Serial, utilisez ce code (arduino/capteur_simule.ino) :

// Exemple Arduino - envoyer T et H simulés
void setup() {
  Serial.begin(115200);
}

void loop() {
  float t = random(180,300) / 10.0; // 18.0 -> 30.0
  float h = random(400,800) / 10.0; // 40 -> 80
  Serial.print("T:");
  Serial.print(t, 2);
  Serial.print(";H:");
  Serial.println(h, 2);
  delay(2000);
}


Ce fichier peut être ouvert dans l’IDE Arduino et téléversé sur la carte.
g
🔹 Structure du dossier
02_LectureSerie_PySerial/
├── .venv/                      # environnement virtuel local (NE PAS pousser sur GitHub)
├── arduino/
│   └── capteur_simule.ino      # code Arduino simulé
├── src/
│   └── lecture_serial.py       # script principal
├── data/
│   └── sample_from_serial.csv  # petit échantillon ou généré par le script
├── screenshots/
│   └── screenshot_console_serial_01.png
├── README.md
└── requirements.txt


Tous les résultats (CSV et captures d’écran) sont stockés dans les dossiers respectifs.
Le script lecture_serial.py gère automatiquement la création de data/sample_from_serial.csv.

🔹 Notes

Installer les dépendances via :

pip install -r requirements.txt


- Le module pyserial est nécessaire pour le mode Arduino.


---
