MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9',
         '......': '.', '.-.-.-': ',', '---...': ':',
         '-.-.-.': ';', '-.--.-': '|', '.----.': "'",
         '.-..-.': '"', '-....-': '-', '-..-.': "/",
         '..--.-': '_', '..--..': '?', '--..--': "!",
         '.-.-.': '+', '-...-': '\\', '........': "~",
         '.--.-.': '@', '..-.-': '\n'
         }
MORSE_RUS = {'.-':    'а', '-...':  'б', '-.-.':  'ц',
             '-..':   'д', '.':     'е', '..-.':  'ф',
             '--.':   'г', '....':  'х', '..':    'и',
             '.---':  'й', '-.-':   'к', '.-..':  'л',
             '--':    'м', '-.':    'н', '---':   'о',
             '.--.':  'п', '--.-':  'щ', '.-.':   'р',
             '...':   'с', '-':     'т', '..-':   'у',
             '...-':  'ж', '.--':   'в', '-..-':  'ь',
             '-.--':  'ы', '--..':  'з', '-----': '0',
             '.----': '1', '..---': '2', '...--': '3',
             '....-': '4', '.....': '5', '-....': '6',
             '--...': '7', '---..': '8', '----.': '9',
             '......': '.', '.-.-.-': ',', '---...': ':',
             '-.-.-.': ';', '-.--.-': '|', '.----.': "'",
             '.-..-.': '"', '-....-': '-', '-..-.': "/",
             '..--.-': '_', '..--..': '?', '--..--': "!",
             '.-.-.': '+', '-...-': '\\', '........': "~",
             '.--.-.': '@', '..-.-': '\n', '---.': 'ч',
             '----': 'ш', '--.--': 'ъ', '..-..': 'э', '..--': 'ю',
             '.-.-': 'я'
             }


END_STR = ['.', '!', '?', '\n']


def get_morse():
    return MORSE


def get_morse_rus():
    return MORSE_RUS


def get_help():
    print('help')


def decorator(text):
    text = str(text).lower()
    result_text = ''
    for i in range(len(text)):
        if i == 0:
            result_text += text[i]
            continue
        if text[i] == ' ' and text[i-1] == ' ':
            continue
        elif text[i] == '(' or text[i] == ')':
            result_text += '|'
        else:
            result_text += text[i]
    return result_text


def text_collapse(texts):
    result_text = ''
    if isinstance(texts, dict) and len(texts['en']) == len(texts['ru']):
        for i in range(len(texts['en'])):
            if texts['en'][i] == texts['ru'][i]:
                result_text += texts['en'][i]
            elif texts['en'][i] == '~':
                result_text += texts['ru'][i]
            else:
                result_text += texts['en'][i]
        return result_text
    else:
        return None


def decoder(code, coding=get_morse()):
    words = code.split('   ')
    decode = ''
    for word in words:
        chars = word.split(' ')
        decode_word = ''
        for char in chars:
            if not coding[char] in coding.values():
                continue
            decode_word += coding[char]
        decode += decode_word + ' '
    return decode[:-1]


def _get_key_dict(my_dict: dict, value):
    k: object
    for k, v in my_dict.items():
        if v == value:
            return k
    return '!'


def coder(message, coding=get_morse()):
    message = str(message).lower()
    words = message.split(' ')
    code = ''
    for word in words:
        for i in range(len(word)):
            if not word[i] in coding.values():
                code += str(_get_key_dict(coding, '~')) + ' '
            else:
                code += str(_get_key_dict(coding, word[i])) + ' '
        code = code + '  '
    return code[:-3]


if __name__ == '__main__':
    print("Example:")
    m = coder('Hello, my friends. У нас все хорошо!')
    print(m)
    print(decoder(m))
    m = coder('Hello, my friends. У нас все хорошо!', coding=MORSE_RUS)
    print(m)
    print(decoder(m, coding=MORSE_RUS))
    print(decoder('... --- ...'))
    print(decoder("..--- ----- .---- ---.."))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decoder("... --- -- .   - . -..- -") == "some text"
    assert decoder("..--- ----- .---- ---..") == "2018"
    assert decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "it was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
