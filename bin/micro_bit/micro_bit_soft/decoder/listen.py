from microbit import *
import music

while True:
    if pin1.read_digital() == 1:
        music.pitch(440, 50, wait=False)
        display.set_pixel(2, 2, 9)
    else:
        display.clear()
        music.stop()
