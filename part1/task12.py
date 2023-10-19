def decode_morse_code(q):
    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    decoded_message = ''
    words = q.split('   ')  # Разделение кода на слова (положим три пробела между словами)
    for word in words:
        letters = word.split(' ')  # Разделение слова на буквы (положим один пробел между буквами)
        for letter in letters:
            for key, value in morse_dict.items():
                if value == letter:
                    decoded_message += key
                    break
        decoded_message += ' '

    return decoded_message.strip()


def encode_morse_code(message):
    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    encoded_message = ''
    for char in message:
        if char.upper() in morse_dict:
            encoded_message += morse_dict[char.upper()] + ' '
        elif char == ' ':
            encoded_message += '   '

    return encoded_message.strip()


# morse_code = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
# decoded_message = decode_morse_code(morse_code)
#
# print(decoded_message)
# #
# print(encode_morse_code("CHECK THIS OUT"))

def tests():
    assert decode_morse_code('.... . .-.. .-.. ---   .-- --- .-. .-.. -..')=="HELLO WORLD"
    assert decode_morse_code("-.-. .... . -.-. -.-    - .... .. ...    --- ..- -")=="CHECK THIS OUT"
    print("ok")
tests()