from microbit import *
import music

while True:
    if button_a.is_pressed():
        pin1.write_digital(True)
    elif pin2.read_digital() == 1:
        music.pitch(440, 50, wait=False)
    else:
        music.stop()
        pin1.write_digital(False)
