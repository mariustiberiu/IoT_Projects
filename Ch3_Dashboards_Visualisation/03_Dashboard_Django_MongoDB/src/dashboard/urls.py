from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_view, name="dashboard"),
    path("api/data", views.api_data, name="api_data"),
    path("insert", views.insert_data, name="insert_data"),
    path("capteurs", views.capteurs_view, name="capteurs_view"),  # 👈 nouvelle route
    path("dernieres_lectures_api/", views.dernieres_lectures_api, name="dernieres_lectures_api"),  # 👈 nouvelle route
    path("export_csv/", views.export_csv, name="export_csv"),  # 👈 nouvelle route pour l'export CSV
    path("export_json/", views.export_json, name="export_json"),  # 👈 nouvelle route pour l'export JSON
]
