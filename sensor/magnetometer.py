from machine import I2C, Pin
import math


class Magnetometer:
    """Class to manage sensor interaction"""

    def __init__(self):
        self.sda = Pin(4)
        self.scl = Pin(5)
        self.i2c = I2C(sda=self.sda, scl=self.scl, freq=100000)
        self.address = self.i2c.scan()[0]

        self.regB = 0xE0
        self.gain = 0.435

        self.i2c.writeto_mem(self.address, 1, bytearray([self.regB]))

        self.x = 0
        self.y = 0
        self.z = 0

    def twosCompConv(self, numA, numB):
        if numA >= 128:
            return -((~((numA << 8) | numB)) & 0xFFFF)
        else:
            return (numA << 8) | numB

    def take_measurement(self):
        self.i2c.writeto_mem(self.address, 2, bytearray([0x01]))
        res = self.i2c.readfrom_mem(self.address, 3, 6)

        self.x = self.twosCompConv(res[0], res[1]) * self.gain
        self.z = self.twosCompConv(res[2], res[3]) * self.gain
        self.y = self.twosCompConv(res[4], res[5]) * self.gain
        #return (self.x, self.y, self.z)
        #print(math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z))


class Lock:
    """Convert reading from the magenetometer"""
    def __init__(self):
        self.magnetometer=Magnetometer()


