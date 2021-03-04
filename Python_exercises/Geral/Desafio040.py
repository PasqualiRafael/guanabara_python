from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Média de alunos')

# input
n1 = float(input(f'Qual sua primeira nota? \n'))
n2 = float(input(f'Digite sua segunda nota: \n'))

# calc
_media = (n1 + n2) / 2

# condition
if _media < 5:
    print('{}Reprovado{}'.format(cores['red'], cores['close']))
elif 5 <= _media <= 6.9:
    print('{}Recuperação{}'.format(cores['yellow'], cores['close']))
else:
    print('{}Aprovado{}'.format(cores['green'], cores['close']))




pasqualiFinal.close()
