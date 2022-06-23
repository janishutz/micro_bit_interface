import maqueen_driver
import microbit
import music

md = maqueen_driver.Driver()

class FollowTheLine:
    def __init__(self):
        self.__activated = 0

    def run(self):
        while True:
            if md.getDistance() < 20:
                md.stop()
                md.setLEDs(on=1)
                music.pitch(440, 20)
            else:
                if md.getLineTracker(1) == 0:
                    self.__activated = 0
                    md.motor(0, 100, 0, 255)
                elif md.getLineTracker(2) == 0:
                    self.__activated = 0
                    md.motor(0, 255, 0, 100)
                else:
                    if self.__activated <= 50:
                        self.__activated += 1
                        md.motor(0, 140, 0, 140)
                    else:
                        md.motor(0, 255, 0, 255)
