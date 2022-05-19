import music
from microbit import *

while True:
    if button_a.is_pressed() is True:
        pin1.write_digital(1)
        music.pitch(440, 50, wait=False)
    else:
        music.stop()
        pin1.write_digital(0)

