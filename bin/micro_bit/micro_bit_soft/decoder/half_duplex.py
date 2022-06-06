from microbit import *
import music

while True:
    if button_a.is_pressed() is True:
        if pin1.read_digital() == 1:
            display.show(Image.NO)
        else:
            pin1.write_digital(1)
    else:
        music.stop()
        pin1.write_digital(0)
        if pin1.read_digital() == 1:
            music.pitch(440, 50, wait=False)
        else:
            music.stop()
