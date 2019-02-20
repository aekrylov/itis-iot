from time import sleep

import pigpio

pi = pigpio.pi('10.42.0.157')


class KY040:
    CLOCKWISE = 0
    ANTICLOCKWISE = 1

    def __init__(self, clockPin, dataPin, switchPin,
                 rotaryCallback, switchCallback):
        # persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        # setup pins
        pi.set_mode(clockPin, pigpio.INPUT)
        pi.set_mode(dataPin, pigpio.INPUT)
        pi.set_mode(switchPin, pigpio.INPUT)
        # GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        self.clock_cb = pi.callback(self.clockPin, pigpio.FALLING_EDGE, self._clockCallback)
        self.switch_cb = pi.callback(self.switchPin, pigpio.FALLING_EDGE, self._switchCallback)

    def stop(self):
        self.clock_cb.cancel()
        self.switch_cb.cancel()

    def _clockCallback(self, gpio, level, tick):
        if pi.read(self.clockPin) == 0:
            data = pi.read(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)

    def _switchCallback(self, gpio, level, tick):
        if pi.read(self.switchPin) == 0:
            self.switchCallback()


if __name__ == "__main__":

    CLOCKPIN = 13
    DATAPIN = 19
    SWITCHPIN = 26

    count = 0

    def rotaryChange(direction):
        global count
        print("turned - " + str(direction))
        count += -1 if direction else 1
        print('count = %d' % count)


    def switchPressed():
        print("button pressed")

    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN,
                  rotaryChange, switchPressed)

    ky040.start()

    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()

