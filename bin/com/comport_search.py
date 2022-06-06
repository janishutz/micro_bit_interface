import serial.tools.list_ports


class ComportService:
    def __init__(self):
        self.__comport = []
        self.__import = []
        self.__working = []
        self.__pos = 0
        self.__com_name = ""

    def get_comport(self, special_port=""):
        self.__comport = [comport.device for comport in serial.tools.list_ports.comports()]
        self.__pos = 0
        if special_port != "":
            self.__working = special_port
        else:
            print(serial.tools.list_ports.comports())
            while self.__working == []:
                self.__com_name = serial.tools.list_ports.comports()[self.__pos]
                if "NXP ARM mbed" in self.__com_name:
                    self.__working = self.__comport.pop(self.__pos)
                else:
                    self.__pos += 1
        return self.__working
