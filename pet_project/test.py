language = ['русский', 'английский']
do = ['зашифровать', 'дешифровать']


print('Добро пожаловать в программу шифр Цезаря!')
print('Прежде, чем начать, необходимо ответить на несколько вопросов')
print()
qu_1 = input('Алфавит на каком языке необходимо использовать? ')
qu_2 = input('Зашифровать или дешифровать? ')
qu_3 = input('Какой шаг сдвига будем использовать? ')


if qu_1.lower() == 'русский':
    s = ''
    st = input('Введите текст рядом. - ')
    if qu_2.lower() == 'зашифровать':
        for c in st:
            if c in ' ,.?!-0123456789':
                s += c
                continue
            if c.isupper():
                a = ord(c) + int(qu_3)
                if a > 0x042F:
                    a -= 32
                s += chr(a)
            elif c.islower():
                a = ord(c) + int(qu_3)
                if a > 0x044F:
                    a -= 32
                s += chr(a)
    elif qu_2.lower() == 'дешифровать':
        for c in st:
            if c in ' ,.?!-0123456789':
                s += c
                continue
            if c.isupper():
                a = ord(c) - int(qu_3)
                if a < 0x0410:
                    a += 32
                s += chr(a)
            elif c.islower():
                a = ord(c) - int(qu_3)
                if a < 0x0430:
                    a += 32
                s += chr(a)
    print(s)