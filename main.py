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
