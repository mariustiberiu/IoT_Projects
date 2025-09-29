# src/backup_db.py
import sqlite3
import os
import datetime

def backup_db(src="data/capteurs.db", dst_folder="data"):
    if not os.path.exists(src):
        print("Aucune base trouvée à sauvegarder :", src)
        return None
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(dst_folder, f"backup_{ts}.db")
    os.makedirs(dst_folder, exist_ok=True)
    with sqlite3.connect(src) as src_conn:
        with sqlite3.connect(dst) as dst_conn:
            src_conn.backup(dst_conn)
    print("✅ Backup créé :", dst)
    return dst

if __name__ == "__main__":
    backup_db()
