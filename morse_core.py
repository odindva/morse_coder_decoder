MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9',
         '......': '.', '.-.-.-': ',', '---...': ':',
         '-.-.-.': ';', '-.--.-': '|', '.----.': "'",
         '.-..-.': '"', '-....-': '-', '-..-.': "/",
         '..--.-': '_', '..--..': '?', '--..--': "!",
         '.-.-.': '+', '-...-': '\\', '........': "~",
         '.--.-.': '@', '..-.-': '\n', '': ''
         }
MORSE_RUS = {'.-': 'а', '-...': 'б', '-.-.': 'ц',
             '-..': 'д', '.': 'е', '..-.': 'ф',
             '--.': 'г', '....': 'х', '..': 'и',
             '.---': 'й', '-.-': 'к', '.-..': 'л',
             '--': 'м', '-.': 'н', '---': 'о',
             '.--.': 'п', '--.-': 'щ', '.-.': 'р',
             '...': 'с', '-': 'т', '..-': 'у',
             '...-': 'ж', '.--': 'в', '-..-': 'ь',
             '-.--': 'ы', '--..': 'з', '-----': '0',
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
             '.-.-': 'я', '': ''
             }

_END_STR = ['.', '!', '?', '\n']


def _get_morse():
    return MORSE


def _get_morse_rus():
    return MORSE_RUS


def _get_help(full=False):
    if full:
        print(f'{MORSE}\n\\\n{MORSE_RUS}\n')
    print(' code file1/text [file2]    - Кодирует текст или тест из файла-1. '
          'Закодированный текст возвращает (если нет параметра-2) сохраняет в файл-2.'
          'Текст кодируется в 2-х экземплярах: 1 - для английских символов, 2 - для русских символов.\n',
          'decode file1/text [file2]  - Декодирует текст или тест из файла-1. '
          'Декодированный текст возвращает (если нет параметра-2) сохраняет в файл-2. '
          'Декодированный текст содержит и английские и русские символы (если они были в сообщении).\n'
          'Если вводить код Морзе самостоятельно, то 1 пробел - разделитель символов, 3 пробела - разделитель слов\n',
          'help  - Помощь. При вызове по команде показывает азбуку Морзе')


def _decorator(text):
    text = str(text).lower()
    result_text = ''
    for i in range(len(text)):
        if i == 0:
            result_text += text[i]
            continue
        if text[i] == ' ' and text[i - 1] == ' ':
            continue
        elif text[i] == '(' or text[i] == ')':
            result_text += '|'
        else:
            result_text += text[i]
    return result_text


def _text_collapse(texts):
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


def _decoder(code, coding=_get_morse()):
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


def _coder(message, coding=_get_morse()):
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
    m = _coder('Hello, my friends. У нас все хорошо!')
    print(m)
    print(_decoder(m))
    m = _coder('Hello, my friends. У нас все хорошо!', coding=MORSE_RUS)
    print(m)
    print(_decoder(m, coding=MORSE_RUS))
    print(_decoder('... --- ...'))
    print(_decoder("..--- ----- .---- ---.."))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert _decoder("... --- -- .   - . -..- -") == "some text"
    assert _decoder("..--- ----- .---- ---..") == "2018"
    assert _decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "it was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
