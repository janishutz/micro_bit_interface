import microbit
import radio
import basic_filtering
import struct


bf = basic_filtering.BasicFiltering()


class RadioCom:
    def __init__(self):
        microbit.uart.init(19200)

    def run(self, group):
        radio.config(group=group)
        radio.on()

    def inst(self):
        pass

    def sendpc(self, info):
        microbit.uart.write(info)

    def listen(self):
        # listens for messages, sends received text to PC if possible
        # also returns value, None, if no data is being received
        radio.receive()

    def send(self, message):
        radio.send(str(message))
