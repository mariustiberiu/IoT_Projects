# recevoir un message dans la console.

import paho.mqtt.client as mqtt

broker = "localhost"
topic = "sensors/manual"
msg = "Caa marche .. i love ya baby😊"

client = mqtt.Client()
client.connect(broker, 1883)
client.publish(topic, msg)
client.disconnect()
print(f"Message publié sur {topic}: {msg}")