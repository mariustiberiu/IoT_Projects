from django.shortcuts import render
from .models import SensorData
import pandas as pd
import plotly.express as px
from django.http import JsonResponse
# from mongo_connection import capteurs  # on importe notre collection MongoDB
from . import mongo_connection
from bson import ObjectId
from .mongo_connection import capteurs
from datetime import datetime
import plotly.io as pio
import csv
from django.http import HttpResponse
import json
import os
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from datetime import datetime
import pandas as pd
from . import mongo_connection
import os
import json
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from datetime import datetime
import os
import csv
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse



def dashboard_view(request):
    capteurs = mongo_connection.capteurs
    donnees_raw = list(capteurs.find().sort("timestamp", -1))  # toutes les lectures

    # Convertir en DataFrame
    if donnees_raw:
        df = pd.DataFrame(donnees_raw)
        df['id'] = df['_id'].astype(str)  # pour éviter _id dans le template
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    else:
        df = pd.DataFrame(columns=['id', 'sensor_name', 'temperature', 'humidite', 'timestamp'])

    # Graphique Température
    fig_temp = px.line(df, x='timestamp', y='temperature', color='sensor_name',
                       title="Température des capteurs", markers=True)
    fig_temp.update_layout(height=400)  # plus grand
    plot_temp = pio.to_html(fig_temp, full_html=False)

    # Graphique Humidité
    fig_hum = px.line(df, x='timestamp', y='humidite', color='sensor_name',
                      title="Humidité des capteurs", markers=True)
    fig_hum.update_layout(height=400)  # plus grand
    plot_hum = pio.to_html(fig_hum, full_html=False)

    # Dernières lectures (10 dernières)
    last_rows = df.sort_values('timestamp', ascending=False).head(10).to_dict('records')

    # Liste des capteurs uniques pour le filtre
    capteurs_uniques = df['sensor_name'].unique().tolist() if not df.empty else []

    context = {
    'plot_temp': plot_temp,
    'plot_hum': plot_hum,
    'donnees': df.to_dict('records'),
    'rows': last_rows,
    'capteurs_uniques': capteurs_uniques
        }

    
    return render(request, 'dashboard/dashboard.html', context)

# API pour les dernières lectures en JSON (rafraîchissement Ajax)
# API pour les dernières lectures en JSON (rafraîchissement Ajax)
def dernieres_lectures_api(request):
    capteurs = mongo_connection.capteurs  # 👈 réutilise la connexion ouverte
    donnees_raw = list(capteurs.find().sort("timestamp", -1).limit(50))

    rows = []
    for doc in donnees_raw:
        rows.append({
            "sensor_name": doc.get("sensor_name", "").strip().lower(),
            "temperature": doc.get("temperature"),
            "humidite": doc.get("humidite"),
            "timestamp": doc.get("timestamp").strftime("%Y-%m-%d %H:%M:%S") if "timestamp" in doc else ""
        })
    return JsonResponse({"rows": rows})

# API simple pour récupérer JSON (ex : /api/data?limit=50)
def api_data(request):
    limit = int(request.GET.get("limit", 100))
    docs = SensorData.objects.order_by("-timestamp").limit(limit)
    out = []
    for d in docs:
        out.append({
            "sensor_name": d.sensor_name,
            "temperature": d.temperature,
            "humidity": d.humidity,
            "timestamp": d.timestamp.isoformat()
        })
    return JsonResponse(out, safe=False)

def export_csv(request):
    capteurs = mongo_connection.capteurs
    # Filtrage par capteur si fourni
    capteur_filtre = request.GET.get("capteur")
    if capteur_filtre:
        donnees_raw = list(capteurs.find({"sensor_name": capteur_filtre}))
    else:
        donnees_raw = list(capteurs.find())

    # Préparer le CSV
    response = HttpResponse(content_type='text/csv')
    filename = f"capteurs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    writer.writerow(['id', 'sensor_name', 'temperature', 'humidite', 'timestamp'])
    for doc in donnees_raw:
        writer.writerow([
            str(doc['_id']),
            doc.get('sensor_name', ''),
            doc.get('temperature', ''),
            doc.get('humidite', ''),
            doc['timestamp'].strftime("%Y-%m-%d %H:%M:%S") if 'timestamp' in doc else ''
        ])
    return response

def export_json(request):
    capteurs = mongo_connection.capteurs
    capteur_filtre = request.GET.get("capteur")
    if capteur_filtre:
        donnees_raw = list(capteurs.find({"sensor_name": capteur_filtre}))
    else:
        donnees_raw = list(capteurs.find())

    # Conversion types non JSON sérialisables
    for doc in donnees_raw:
        doc['_id'] = str(doc['_id'])
        if 'timestamp' in doc and isinstance(doc['timestamp'], datetime):
            doc['timestamp'] = doc['timestamp'].strftime("%Y-%m-%d %H:%M:%S")

    # Chemin fichier
    filename = f"capteurs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    export_path = os.path.join(settings.BASE_DIR, 'export', filename)
    os.makedirs(os.path.dirname(export_path), exist_ok=True)

    with open(export_path, 'w', encoding='utf-8') as f:
        json.dump(donnees_raw, f, indent=4, ensure_ascii=False)

    return JsonResponse({'message': f'Données exportées avec succès dans {export_path}'})

def insert_data(request):
    data = {"temperature": 25, "humidite": 60}
    mongo_connection.capteurs_collection.insert_one(data)
    return JsonResponse({"message": "Donnée insérée avec succès ✅"})

def capteurs_view(request):
    # Récupérer toutes les données depuis MongoDB
    donnees = list(capteurs.find())
    # Transformer les ObjectId en string (sinon Django n'aime pas)
    for doc in donnees:
        doc["_id"] = str(doc["_id"])
    return render(request, "dashboard.html", {"donnees": donnees})



