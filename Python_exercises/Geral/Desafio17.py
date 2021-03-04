from modulos import pasqualiFinal
from math import hypot

pasqualiFinal.ini(f'Triangulo Hiptenusa')

user_x = int(input(f'Qual o tamanho da base do triangulo?\n'))
user_y =  int(input(f'Qual o tamanho da altura do triangulo?\n'))

print('A hipotenusa é: {}'.format(hypot(user_x, user_y)))

pasqualiFinal.close()