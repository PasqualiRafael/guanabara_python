from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Comparação de dois numero inteiros')

# input
n1 = int(input(f'Digite um numero:\n'))
n2 = int(input(f'Digite um numero:\n'))

# condition
if n1 > n2:
    print('O primeiro valor {}Maior{}'.format(cores['blue'], cores['close']))
elif n2 > n1:
    print('O segundo valor é {}Maior{}'.format(cores['blue'], cores['close']))
else:
    print('Os valores são {}Iguais{}'.format(cores['blue'], cores['close']))


pasqualiFinal.close()
