import music

import encoder
import music


mdc = encoder.Encoder()


class Morse:
    def __init__(self):
        self.__encoded = []
        self.__sound_duration = 50

    def run(self):
        self.__encoded = mdc.encode()
        self.output_gen()

    def output_gen(self):
        for self.item in self.__encoded:
            for self.ec in self.item:
                if self.ec == ".":
                    music.pitch(440, self.__sound_duration)
                elif self.ec == "-":
                    music.pitch(440, self.__sound_duration * 3)


Morse().run()
