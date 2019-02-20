from time import sleep

import pigpio

from rotary_counter import KY040

pi = pigpio.pi('10.42.0.157')  # PI host where pigpiod is running

LASER_PIN = 17  # Signal pin of a laser, BCM numeration
CLOCKPIN = 13
DATAPIN = 19
SWITCHPIN = 26

pi.set_mode(LASER_PIN, pigpio.OUTPUT)
pi.set_PWM_range(LASER_PIN, 50)

count = 0


def rotary_change(direction):
    global count
    count += -1 if direction else 1
    print('count = %d' % count)
    if count > 50:
        count = 50
    pi.set_PWM_dutycycle(LASER_PIN, max(count, 0))


def switch_pressed():
    global count
    print("button pressed")
    count = 0
    pi.set_PWM_dutycycle(LASER_PIN, max(count, 0))


ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotary_change, switch_pressed)
ky040.start()

try:
    while True:
        sleep(0.1)
finally:
    ky040.stop()
    pi.set_PWM_dutycycle(LASER_PIN, 0)
