import serial
import time
import bin.com.lib


lb = bin.com.lib.Com()


class CommandListGenerator:
    def __init__(self):
        self.__go = 0
        self.__received = ""
        self.__start = 0
        self.__lfcount = 0
        self.__total = ""
        self.__output = []

    def run(self, special_port):
        # This function asks the micro:bit to send a list of all of the commands the program that runs
        # on it supports. Sent string: "\ncmdl\n". Please note: if using micropython, use the here included
        # com module to communicate (you can flash it to the micro:bit through the settings menu and also
        # add your own modules to the micro:bit.
        try:
            lb.connect(19200, special_port)
            self.__go = 1
        except serial.SerialException as e:
            return e
        if self.__go == 1:
            self.__start = time.time()
            lb.send("\ncmdl\n")
            self.__go = 0
            while time.time() - self.__start < 5:
                self.__received = lb.receive(1)
                if self.__received == "\n":
                    self.__received = lb.receive(1)
                    if self.__received == "c":
                        self.__received = lb.receive(1)
                        if self.__received == "m":
                            self.__received = lb.receive(1)
                            if self.__received == "d":
                                self.__go = 1
                                break
        if self.__go == 1:
            self.__total = ""
            self.__output = []
            lb.receive(1)
            while self.__lfcount < 3:
                self.__received = lb.receive(1)
                if self.__received == "\n":
                    self.__lfcount += 1
                else:
                    self.__lfcount = 0
                    if self.__received == " ":
                        self.__output.append(self.__total)
                        self.__total = ""
                    else:
                        self.__total += self.__received
            return self.__output
