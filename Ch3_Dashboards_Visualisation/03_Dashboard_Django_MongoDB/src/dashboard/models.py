from django.db import models

# Create your models here.
from mongoengine import Document, StringField, FloatField, DateTimeField, connect
from django.conf import settings

# Connect at import time using settings values
connect(
    db=settings.MONGO_DB_NAME,
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
    username=settings.MONGO_USERNAME or None,
    password=settings.MONGO_PASSWORD or None,
    alias="default",
)

class SensorData(Document):
    meta = {"collection": "sensor_data"}
    sensor_name = StringField(required=True, default="sensor_1")
    temperature = FloatField(required=True)
    humidity = FloatField(required=True)
    timestamp = DateTimeField(required=True)
