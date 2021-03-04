from modulos import pasqualiFinal
from modulos.colors import cores
from time import sleep

pasqualiFinal.ini('Calculadora')

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('')
result = 0
user = 0
rodar = False

while not rodar:
    user = int(input(
        '{}[1]{}Somar\n'.format(cores['blue'], cores['close']) +
        '{}[2]{}Multiplicar\n'.format(cores['blue'], cores['close']) +
        '{}[3]{}Maior\n'.format(cores['blue'], cores['close']) +
        '{}[4]{}Novos numeros\n'.format(cores['blue'], cores['close']) +
        '{}[5]{}Sair do programa\n'.format(cores['blue'], cores['close']) +
        'Digite uma opção no menu: \n')
    )
    if user == 1:
        result = v1 + v2
        print('{}{} + {} = {}{}'.format(cores['yellow'], v1, v2, result, cores['close']))
    elif user == 2:
        result = v1 * v2
        print('{}{} * {} = {}{}'.format(cores['yellow'], v1, v2, result, cores['close']))
    elif user == 3:
        print('{}O maior numero é: {}{}'.format(cores['yellow'], max(v1, v2), cores['close']))
    elif user == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif user == 5:
        rodar = True
    else:
        print('Voce precisa digitar uma das opções!')
    print('-=-' * 16)
    sleep(1)


pasqualiFinal.close()
