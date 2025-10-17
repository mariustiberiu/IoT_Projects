import sqlite3

# Chemin vers ta base de données
db_path = r"D:\Django\Nouveau dossier\IoT_Projects\Ch1_Acquisition_Données_Capteurs\03_Stockage_SQLite\data\capteurs.db"

# Connexion à la base SQLite
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 1️⃣ Créer la table si elle n'existe pas
cur.execute("""
CREATE TABLE IF NOT EXISTS mesures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    humidite REAL,
    source TEXT DEFAULT 'simulation'
)
""")

# 2️⃣ Vérifier si la colonne 'source' existe
cur.execute("PRAGMA table_info(mesures)")
colonnes = [col[1] for col in cur.fetchall()]

if 'source' not in colonnes:
    print("La colonne 'source' est manquante, ajout en cours...")
    cur.execute("ALTER TABLE mesures ADD COLUMN source TEXT DEFAULT 'simulation'")
    print("Colonne 'source' ajoutée avec succès !")
else:
    print("La colonne 'source' existe déjà.")

# 3️⃣ Afficher la structure finale de la table
cur.execute("PRAGMA table_info(mesures)")
for col in cur.fetchall():
    print(col)

conn.commit()
conn.close()

