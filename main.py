import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

num = int(input('Сколько нужно паролей?'))
leng = int(input('Какая будет длина пароля?'))
dig = input('Включать ли цифры 0123456789? (д = да, н = нет)')
up = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д = да, н = нет)')
low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д = да, н = нет)')
sym = input('Включать ли символы !#$%&*+-=?@^_? (д = да, н = нет)')
isk = input('Исключать ли неоднозначные символы il1Lo0O? (д = да, н = нет)')

if dig == 'д':
    chars += digits
if up == 'д':
    chars += uppercase_letters
if low == 'д':
    chars += lowercase_letters
if sym == 'д':
    chars += punctuation
for i in range(int(num)): # старт программы
    if isk == 'д':
        for i in range(int(leng)):
            if chars.count(chars[i]) > 1:
                while chars[i]==random.sample(chars):
                    chars.replace(i, random.sample(chars))
    print(*random.sample(chars, int(leng)), sep='')
#no
