import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "venkatesh/test/mqtt"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

client.loop_start()

for i in range(1, 6):

    message = f"Hello MQTT {i}"

    result = client.publish(TOPIC, message, qos=1)

    if result.rc == mqtt.MQTT_ERR_SUCCESS:
        print("Published:", message)
    else:
        print("Publish failed")

    time.sleep(2)

client.loop_stop()
client.disconnect()