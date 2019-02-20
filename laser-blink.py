from time import sleep

import pigpio

pi = pigpio.pi('10.42.0.157')

PIN = 17  # Signal pin of a laser, BCM numeration
pi.set_mode(PIN, pigpio.OUTPUT)

while True:
    pi.write(17, 1)
    sleep(1)
    pi.write(17, 0)
    sleep(1)
