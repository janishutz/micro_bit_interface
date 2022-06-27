import maqueen_driver

md = maqueen_driver.Driver()


class FollowTheLine:
    def __init__(self):
        self.__activated = 0
        self.__repeated = 0

    def run(self):
        while True:
            if md.getLineTracker(1) == 0:
                self.__activated = 0
                if self.__repeated >= 75 and self.__repeated < 150:
                    self.__repeated += 1
                    md.motor(0, 10, 0, 100)
                elif self.__repeated >= 100:
                    md.motor(0, 0, 0, 100)
                else:
                    self.__repeated += 1
                    md.motor(0, 50, 0, 100)
            elif md.getLineTracker(2) == 0:
                self.__activated = 0
                self.__repeated += 1
                if self.__repeated >= 75 and self.__repeated < 150:
                    self.__repeated += 1
                    md.motor(0, 100, 0, 10)
                elif self.__repeated >= 100:
                    md.motor(0, 100, 0, 0)
                else:
                    self.__repeated += 1
                    md.motor(0, 100, 0, 50)
            else:
                self.__repeated = 0
                if self.__activated <= 2000:
                    self.__activated += 1
                    md.motor(0, 100, 0, 100)
                else:
                    md.motor(0, 255, 0, 255)
