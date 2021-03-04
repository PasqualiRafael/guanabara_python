from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Calculo do Indice de Massa Corporea(IMC)')

# input
altura = int(input(f'Qual sua altura em cm:\n'))
peso = float(input(f'Qual sua massa: \n'))

# calc
altura = altura / 100
imc = peso / altura ** 2

# condtion
if imc < 18.5:
    print('{}Abaixo do peso{}'.format(cores['blue'], cores['close']))
elif 18.5 <= imc < 25:
    print('{}Peso ideal{}'.format(cores['blue'], cores['close']))
elif 25 <= imc < 30:
    print('{}Sobrepeso{}'.format(cores['blue'], cores['close']))
elif 30 <= imc < 40:
    print('{}Obesidade{}'.format(cores['blue'], cores['close']))
else:
    print('{}Obesidade mórbida{}'.format(cores['blue'], cores['close']))
print('Seu imc: {}{:.2f}{}'.format(cores['yellow'], imc, cores['close']))


pasqualiFinal.close()
