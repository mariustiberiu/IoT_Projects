# 02 - Lecture via port série (PySerial)

## 🎯 Objectif
Lire des mesures depuis un port série (Arduino/ESP) ou simuler des mesures localement.
Enregistrer les valeurs dans `data/sample_from_serial.csv`.

## 🛠 Technologies
- Python 3.13
- pyserial (optionnel si vous utilisez le port réel)

## Structure

--------------------------------

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