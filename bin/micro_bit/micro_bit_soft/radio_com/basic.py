import microbit
import radio


class Basic:
    def __init__(self):
        self.__rx = ""
        self.__decode = 0
        self.__go = 0
        self.d = 0
        self.__x = 0
        self.__y = 0

    def run(self, group):
        radio.config(group=group)
        radio.on()
        while True:
            self.receive_p()

    def receive_p(self):
        self.__rx = radio.receive()
        try:
            self.__decode = int(self.__rx)
            self.__go = 1
        except TypeError:
            pass

        if self.__go == 1:
            for self.i in range(self.__decode):
                self.d = self.i / 2
                self.__y = self.d % 4
                self.__x = self.d // 4
                if self.__x and self.__y < 4:
                    microbit.display.set_pixel(self.__x, self.__y, 9)
                else:
                    pass
        else:
            pass


m = Basic()
m.run(11)
