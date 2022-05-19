# create class that encodes plain text into morse

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

    def encode(self):
        self.__input_raw = self.get_input()
        for self.item in self.__input_raw:
            self.__code = self.morse_code.get(self.item)
            self.__output.append(self.__code)
        return self.__output

    def get_input(self):
        return input("please input some text here to transmit: ").upper()
