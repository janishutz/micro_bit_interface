import maqueen_driver

md = maqueen_driver.Driver()


class FollowTheLineDumnb:
    def __init__(self):
        pass

    def run(self):
        while True:
            if md.getLineTracker(1) == 1:
                md.motor(0, 10, 0, 75)
            elif md.getLineTracker(2) == 2:
                md.motor(0, 75, 0, 10)
            else:
                md.motor(0, 75, 0, 75)
