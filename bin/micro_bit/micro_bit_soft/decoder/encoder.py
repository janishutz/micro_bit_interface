# create class that encodes plain text into morse
import microbit


class Encoder:
    # init class
    def __init__(self):
        # Morse code dict
        self.morse_code = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', 'Ä': '.-.-', 'Ö': '---.',
                      'Ü': '..--', ',': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', ':': '---...',
                      '!': '-.-.--', ' ': '@'}
        self.__input_raw = ""
        self.__output = []
        self.__pos = 0
        self.check = 0

    def encode(self):
        self.__input_raw = self.get_input()
        for self.item in self.__input_raw:
            self.__code = self.morse_code.get(self.item)
            self.__output.append(self.__code)
        return self.__output

    def get_input(self):
        self.str_input = "Please type the text to be morsed. "
        microbit.uart.write(self.str_input.encode())
        self.input = ""
        while self.input == "":
            self.input = microbit.uart.read(1)

        self.ouput = ""
        self.check = 0

        while self.check < 3:
            self.input = microbit.uart.read(1)
            if self.input == "":
                self.output += self.input
                self.check += 1
            else:
                self.ouput += self.input
        return self.ouput
