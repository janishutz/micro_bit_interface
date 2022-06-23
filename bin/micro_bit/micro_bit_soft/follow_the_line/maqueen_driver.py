from microbit import *
import machine


class Driver:
    # Maqueen motor control
    # direction:0=forward  1=back
    # speed：0~255
    def __init__(self):
        self._v = 127
        self.i2cAddr = 0x10
        self.FORW = 0
        self.BACK = 1
        self.s = 0.069

    def motor(self, directionL, speedL, directionR, speedR):
        self.buf = bytearray(5)
        self.buf[0] = 0x00 # offset
        self.buf[1] = directionL
        self.buf[2] = speedL
        self.buf[3] = directionR
        self.buf[4] = speedR
        try:
            i2c.write(self.i2cAddr, self.buf)
        except:
            print("Please switch on mbRobot!")
            while True:
                pass

    def motorL(self, directionL, speedL):
        self.buf = bytearray(3)
        self.buf[0] = 0x00 # offset
        self.buf[1] = directionL
        self.buf[2] = speedL
        try:
            i2c.write(self.i2cAddr, self.buf)
        except:
            print("Please switch on mbRobot!")
            while True:
                pass

    def motorR(self, directionR, speedR):
        self.buf = bytearray(3)
        self.buf[0] = 0x02 # offset
        self.buf[1] = directionR
        self.buf[2] = speedR
        try:
            i2c.write(self.i2cAddr, self.buf)
        except:
            print("Please switch on mbRobot!")
            while True:
                pass

    # set speed in percentage (0..100)
    def setSpeed(self, speed):
        self._v = abs(speed) * 255 // 100

    def forward(self):
        self.motor(self.FORW, self._v, self.FORW, self._v)

    def backward(self):
        self.motor(self.BACK, self._v, self.BACK, self._v)

    def stop(self):
        self.motor(self.FORW, 0, self.FORW, 0)

    def right(self):
        self.motor(self.FORW if self._v > 0 else self.BACK, self._v * 675 // 1000, self.BACK if self._v > 0 else self.FORW, self._v * 675 // 1000)

    def left(self):
        self.motor(self.BACK if self._v > 0 else self.FORW, self._v * 675 // 1000, self.FORW if self._v > 0 else self.BACK, self._v * 675 // 1000)

    def rightArc(self, r):
        self.vo = self._v
        self.vi = 0
        if r > self.s:
            self.vi = round(self._v * ((r - self.s) / (r + self.s) * (1 - self._v * self._v / 200000)))
        self.motor(self.FORW, self.vo, self.FORW, self.vi)

    def leftArc(self, r):
        self.vo = self._v
        self.vi = 0
        if r > self.s:
            self.vi = round(self._v * ((r - self.s) / (r + self.s) * (1 - self._v * self._v / 200000)))
        self.motor(self.FORW, self.vi, self.FORW, self.vo)

    def setLeftLED(self, on):
        pin8.write_digital(on)

    def setRightLED(self, on):
        pin12.write_digital(on)

    # index：the corresponding line-tracking sensor (1=left, 2=right)
    # returns 0 for black underground and 1 for white underground
    def getLineTracker(self, index):
        if (index == 1):
            return pin13.read_digital()
        if (index == 2):
            return pin14.read_digital()

    def setLEDs(self, on):
        self.setLeftLED(on)
        self.setRightLED(on)

    def getDistance(self):
        # Send a pulse on pin 1
    #     pin1.write_digital(0)
    #     sleep(0.002)
        pin1.write_digital(1)
    #     sleep(0.010)
        pin1.write_digital(0)

        self.pulse_us = machine.time_pulse_us(pin2, 1)
        if (self.pulse_us < 0):
            return 0
        # ((pulse_us / 1000000) * 341) / 2 * 100
        return self.pulse_us * 0.01705