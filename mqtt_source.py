import time

import paho.mqtt.client as paho
from RPi import GPIO

from encodergpio import EncoderGpio

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    CLOCK_PIN = 13
    DATA_PIN = 19
    SWITCH_PIN = 26

    client = paho.Client(client_id="itis_iot_encoder")
    client.connect("broker.mqttdashboard.com", 1883)

    def on_click():
        print("Click!")
        # qos 1 is optimal for reliability/latency
        msg_info = client.publish("rotary/click", qos=1)

        # test message delivery time
        t = time.time()
        msg_info.wait_for_publish()
        print(time.time() - t)

    ky040 = EncoderGpio(CLOCK_PIN, DATA_PIN, SWITCH_PIN, switchCallback=on_click, switchBouncetime=100)
    ky040.start()

    try:
        client.loop_forever()
    finally:
        ky040.stop()
