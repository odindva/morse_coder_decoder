import sys
from morse_core import get_morse, get_morse_rus, coder, decoder, get_help, decorator, text_collapse


commands = ['code',
            'decode',
            'help']
command = None
isCommand = False
param1 = None
param2 = None


try:
    command = sys.argv[1]
    if command in commands:
        isCommand = True
except IndexError:
    command = None

try:
    param1 = sys.argv[2]
except IndexError:
    param1 = None

try:
    param2 = sys.argv[3]
except IndexError:
    param2 = None


if isCommand:
    if command == 'code':
        coded_texts = {'en': '', 'ru': ''}
        if param1:
            try:
                with open(param1, 'r', encoding='utf-8') as f:
                    text = decorator(f.read())
                    coded_texts['en'] = coder(text)
                    coded_texts['ru'] = coder(text, coding=get_morse_rus())
            except FileNotFoundError:
                coded_texts['en'] = coder(decorator(param1))
                coded_texts['ru'] = coder(decorator(param1), coding=get_morse_rus())
            except FileExistsError:
                coded_texts['en'] = coder(decorator(param1))
                coded_texts['ru'] = coder(decorator(param1), coding=get_morse_rus())
        else:
            print('\nвведите строку или имя файла\n')
            get_help()
        if param2:
            try:
                with open(param2, 'w', encoding='utf-8') as f:
                    f.write(coded_texts['en'] + '\n\\\n' + coded_texts['ru'])
            except FileNotFoundError:
                print(coded_texts['en'] + '\n\\\n' + coded_texts['ru'])
            except FileExistsError:
                print(coded_texts['en'] + '\n\\\n' + coded_texts['ru'])
        else:
            print(coded_texts['en'] + '\n\\\n' + coded_texts['ru'])

    elif command == 'decode':
        decoded_texts = {'en': '', 'ru': ''}
        if param1:
            try:
                with open(param1, 'r', encoding='utf-8') as f:
                    texts = f.read().split('\n\\\n')
                    decoded_texts['en'] = decoder(texts[0])
                    decoded_texts['ru'] = decoder(texts[1], coding=get_morse_rus())
            except FileNotFoundError:
                decoded_texts['en'] = decoder(param1)
                decoded_texts['ru'] = decoder(param1, coding=get_morse_rus())
            except FileExistsError:
                decoded_texts['en'] = decoder(param1)
                decoded_texts['ru'] = decoder(param1, coding=get_morse_rus())
        else:
            print('\nвведите строку или имя файла\n')
            get_help()
        if param2:
            try:
                with open(param2, 'w', encoding='utf-8') as f:
                    f.write(text_collapse(decoded_texts))
            except FileNotFoundError:
                print(text_collapse(decoded_texts))
            except FileExistsError:
                print(text_collapse(decoded_texts))
        else:
            print(text_collapse(decoded_texts))

    elif command == 'help':
        get_help()

else:
    print('\nвведите команду\n')
    get_help()
