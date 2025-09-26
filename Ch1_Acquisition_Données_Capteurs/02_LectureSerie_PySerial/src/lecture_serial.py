import argparse
import csv
import os
import random
import sys
import time

try:
    import serial
    import serial.tools.list_ports
except ImportError:
    serial = None  # Si pyserial pas installé, on gère plus bas

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)
CSV_FILE = os.path.join(DATA_DIR, "sample_from_serial.csv")


def ports_disponibles():
    """Retourne la liste des ports série disponibles."""
    if serial is None:
        return []
    return [p.device for p in serial.tools.list_ports.comports()]
