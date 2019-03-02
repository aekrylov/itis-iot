import paho.mqtt.client as paho

if __name__ == '__main__':
    client = paho.Client(client_id="itis_iot_frontend")
    client.connect("broker.mqttdashboard.com", 1883)

    def on_click(client, userdata, msg):
        print("Click!")

    client.on_message = on_click
    client.subscribe("rotary/click")

    client.loop_forever()
