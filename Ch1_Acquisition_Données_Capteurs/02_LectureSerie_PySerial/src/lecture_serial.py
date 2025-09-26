# Fichier: src/lecture_serial.py

# Lecture série ou simulation pour capteur T/H, écrit CSV
import argparse
import time
import csv
import random
from datetime import datetime

# Essai d'importer pyserial
try:
    import serial
except Exception:
    serial = None

parser = argparse.ArgumentParser(description="Lecture port série (ou simulation) -> CSV")
parser.add_argument("--port", type=str, default=None, help="Port série (ex: COM3 ou /dev/ttyUSB0)")
parser.add_argument("--baud", type=int, default=115200, help="Baud rate (défaut 115200)")
parser.add_argument("--simulate", action="store_true", help="Forcer mode simulation (pas de matériel)")
parser.add_argument("--outfile", type=str, default="data/sample_from_serial.csv", help="Fichier CSV de sortie")
parser.add_argument("--delay", type=float, default=2.0, help="Délai entre mesures (s)")
args = parser.parse_args()

def write_header(fout):
    with open(fout, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidite"])

def append_row(fout, t, temp, hum):
    with open(fout, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([t, temp, hum])

def simulate_loop(fout, delay):
    write_header(fout)
    try:
        while True:
            temp = round(random.uniform(18.0, 30.0), 2)
            hum = round(random.uniform(40.0, 80.0), 2)
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{ts} | T:{temp}°C  H:{hum}%")
            append_row(fout, ts, temp, hum)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nSimulation arrêtée par l'utilisateur.")

def serial_loop(port, baud, fout):
    if serial is None:
        print("pyserial non installé. Lance avec --simulate ou installe pyserial.")
        return
    try:
        ser = serial.Serial(port, baud, timeout=1)
    except Exception as e:
        print("Erreur ouverture port série :", e)
        return

    write_header(fout)
    try:
        print(f"Lecture sur {port} à {baud} bauds. Ctrl+C pour arrêter.")
        while True:
            try:
                line = ser.readline().decode(errors="ignore").strip()
            except Exception:
                line = ""
            if not line:
                continue
            # On accepte plusieurs formats: "T:23.4;H:55.2" ou "23.4,55.2"
            temp = None
            hum = None
            if "T:" in line and "H:" in line:
                try:
                    parts = line.split(";")
                    for p in parts:
                        if p.startswith("T:"):
                            temp = float(p.split("T:")[1])
                        if p.startswith("H:"):
                            hum = float(p.split("H:")[1])
                except:
                    pass
            elif "," in line:
                try:
                    a,b = line.split(",")[:2]
                    temp = float(a)
                    hum = float(b)
                except:
                    pass
            # Si parsable -> écrire et afficher
            if temp is not None and hum is not None:
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{ts} | T:{temp}°C  H:{hum}%   (reçu: {line})")
                append_row(args.outfile, ts, temp, hum)
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur.")
    finally:
        try:
            ser.close()
        except:
            pass

if __name__ == "__main__":
    # Si --simulate OU pas de pyserial installé -> simulation
    if args.simulate or serial is None or args.port is None:
        print("Mode SIMULATION (pas de matériel ou --simulate).")
        simulate_loop(args.outfile, args.delay)
    else:
        serial_loop(args.port, args.baud, args.outfile)