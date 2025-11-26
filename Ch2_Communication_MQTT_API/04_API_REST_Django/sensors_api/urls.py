



# sensors_api/urls.py


from django.urls import path
from .views import SensorDataListCreateView, home
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>API Sensors Running ✅</h1>")


    

urlpatterns = [
    path('', home, name='home'),
    path('data/', SensorDataListCreateView.as_view(), name='sensor-data-list-create'),
]
