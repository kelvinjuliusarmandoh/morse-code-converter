MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

class MorseCodeConverter:
    def __init__(self, command, sentences):
        self.command = command.upper()
        self.sentences = str(sentences.upper())

    def convert_to_x(self):
        """Get the sentences. Then convert that things to Morse Code or otherwise."""
        result = []
        if self.command == 'CONVERT':
            result = [MORSE_CODE_DICT[alpha_char] for alpha_char in list(self.sentences) if alpha_char in MORSE_CODE_DICT]
        elif self.command == 'INVERT':
            print(list(self.sentences))
            for morse_char_in_list in self.sentences.split(" "):
                for char_in_dict, morse_char_in_dict in MORSE_CODE_DICT.items():
                    print(morse_char_in_list, morse_char_in_dict)
                    if morse_char_in_list == morse_char_in_dict:
                        result.append(char_in_dict)
        else:
            raise Exception("This command doesn't exist. Choose 'Convert'/'Invert' !")
        result = ' '.join(result)
        print(f"The text/morse code has successfully {self.command.lower()}: {' '.join(result)}")
        return result







