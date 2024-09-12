class Translator:
    """
    Translate between braille and normal alphabet
    arg: The current string
    """
    arg: str
    braille_to_number: dict[str, str]
    braille_to_letter: dict[str, str]
    letter_to_braille: dict[str, str]
    number_to_braille: dict[str, str]

    def __init__(self, into: str):
        self.arg = into

        self.braille_to_number = {
            'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
            'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0'
        }

        self.braille_to_letter = {
            'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
            'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
            'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
            'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
            'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
            'O..OOO': 'z'
        }

        self.letter_to_braille = {v: k for k, v in self.braille_to_letter.items()}
        self.number_to_braille = {v: k for k, v in self.braille_to_number.items()}


    def translate(self):
        """
        Translate the string from braille to alphabet or vice versa
        """
        if any(char == '.' for char in self.arg):
            self.braille_to_alpha()
        else:
            self.alpha_to_braille()

    def alpha_to_braille(self):
        """
        Translate the string from alphabet to string
        """
        braille_so_far = []
        number_follows = False
        for char in self.arg:
            if char == ' ':
                braille_so_far.append('......')
            elif str.isdigit(char):
                if not number_follows:
                    number_follows = True
                    braille_so_far.append('.O.OOO')
                braille_so_far.append(self.number_to_braille[char])
            elif str.isalpha(char):
                if str.isupper(char):
                    braille_so_far.append('.....O')

                braille_so_far.append(self.letter_to_braille[char.lower()])

        self.arg = ''.join(braille_so_far)

    def braille_to_alpha(self):
        """
        Translate the string from braille to alpha
        """
        word_so_far = []
        capital_follows = False
        number_follows = False
        for i in range(0, len(self.arg), 6):
            current_letter = self.arg[i:i+6]
            char = ''.join(current_letter)

            if char == '......':
                # Space follows
                word_so_far.append(' ')
                number_follows = False
            elif char == '.....O':
                # Capital follows
                capital_follows = True
            elif char == '.O.OOO':
                # number follows
                number_follows = True
            else:
                if number_follows:
                    word_so_far.append(self.braille_to_number[current_letter])
                elif capital_follows:
                    word_so_far.append(self.braille_to_letter[current_letter].upper())
                    capital_follows = False
                else:
                    word_so_far.append(self.braille_to_letter[current_letter])
        self.arg = ''.join(word_so_far)

    def outputter(self):
        """
        Return the arg string
        """
        return self.arg


if __name__ == "__main__":
    import sys
    inputter = ' '.join(sys.argv[1:])
    trans = Translator(inputter)
    trans.translate()
    print(trans.outputter())
