from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Conferir se forma um triangulo as retas, qual o tipo de triangulo')

# input
a = float(input(f'Digite o valor da primeira reta:\n'))
b = float(input(f'Digite o valor da segunda reta:\n'))
c = float(input(f'Digite o valor da terceira reta:\n'))

# condition
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Essas retas {}Formam{} um triangulo'.format(cores['green'], cores['close']))
    # categoria
    if a == b == c:
        print('Esse triangulo é: {}Equilátero{}'.format(cores['blue'], cores['close']))
    elif a != b != c != a:
        print('Esse triangulo é: {}Escaleno{}'.format(cores['blue'], cores['close']))
    else:
        print('Esse triangulo é: {}Isósceles{}'.format(cores['blue'], cores['close']))
else:
    print('Essas retas {}não{} formam um triangulo'.format(cores['red'], cores['close']))




pasqualiFinal.close()
