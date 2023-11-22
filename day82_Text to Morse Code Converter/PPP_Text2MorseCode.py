import re

print('Welcome to my Text to Morse Code converter! -- Adam CHEN JINGHAO')

print('It is a professional portfolio project of 100 days of code\n')

convert = True

while convert:

    to_be_convert = input('Please enter text that want to conver into morse code: \n')

    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', to_be_convert)

    cleaned_string = cleaned_string.upper()
    splited_string = cleaned_string.split()

    international_morse_code = {
        'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..'
    }

    for word in splited_string:
        word.split()
        letters = list(word)
        morse_code_letter = []
        for letter in letters:
            morse_code_letter.append(international_morse_code[letter])
        print(f'{word} --> {morse_code_letter}')

    next_round = input('Do you have more text to convert? Y/N ')
    if next_round == 'N':
        convert = False
        print('See you again!')


