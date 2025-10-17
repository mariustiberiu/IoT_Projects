# src/publish_test.py
import paho.mqtt.publish as publish

publish.single(
    "sensors/temperature",
    payload="23.7",
    hostname="localhost"
)
print("Message MQTT publié : sensors/temperature = 23.7")
