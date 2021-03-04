from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Progressão aritimetica usando while')

termo = int(input('Escolha o termo inicial: '))
razao = int(input('Escolha a razao da PA: '))
print('')
result = 0
cont = 0
maxi_term = 10
opc = False

while cont < maxi_term:
    result = termo + razao
    termo += razao
    cont += 1
    print('{}{} + {} = {}{}'.format(cores['yellow'], termo, razao, result, cores['close']))
    if cont == maxi_term:
        print('')
        while not opc:
            opt = str(input('Voce quer adicionar mais termos? {}[S/N]{}\n'.format(cores['blue'], cores['close']))).upper()
            if opt == 'S':
                more_term = int(input('Digite quantos termos a mais: '))
                print('')
                maxi_term += more_term
            elif opt == 'N':
                opc = True
            else:
                print('Desculpe {}não{} entendi.'.format(cores['red'], cores['close']))

pasqualiFinal.close()
