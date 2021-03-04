from modulos import pasqualiFinal
'''
from math import factorial

user_num = float(input('Digite um numero: '))
print('{}! = {}'.format(user_num, factorial(user_num)))
'''

user_num = int(input('Digite um valor: '))
num = user_num
fact = 1

if num < 0:
    print('Não existe fatorial de numero negativo')
elif num == 0:
    print('O fatorial de zero é 1')
else:
    while num > 0:
        fact *= num
        num -= 1
print('{}! = {}'.format(user_num, fact))