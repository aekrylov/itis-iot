from time import sleep

import pigpio

pi = pigpio.pi('10.42.0.157')  # PI host where pigpiod is running

PIN = 17  # Signal pin of a laser, BCM numeration
pi.set_mode(PIN, pigpio.OUTPUT)

while True:
    pi.write(PIN, 1)
    sleep(1)
    pi.write(PIN, 0)
    sleep(1)
