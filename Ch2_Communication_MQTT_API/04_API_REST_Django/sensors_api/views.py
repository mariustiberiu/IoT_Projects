from rest_framework import generics
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataListCreateView(generics.ListCreateAPIView):
    queryset = SensorData.objects.all().order_by('-timestamp')
    serializer_class = SensorDataSerializer
