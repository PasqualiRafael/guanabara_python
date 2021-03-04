from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Sexo e idade ilimitado com break')

idade = h = f = p18 = f20 = h_cadas = 0
sexo = ''
cont = ''

while True:

    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: [M/F] ')).upper().strip()[0]

    if idade >= 18:
        p18 += 1

    while sexo not in 'MF':
        sexo = str(input('Qual o sexo: [M/F] ')).upper().strip()[0]

    if sexo in 'M':
        h_cadas += 1
    else:
        if idade <= 20:
            f20 += 1

    cont = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]

    while cont not in 'SN':
        print('Escolha uma das opções:')
        cont = str(input('Deseja continuar: [S/N] ')).upper().strip()[0]

    if cont in 'N':
        break
    else:
        continue

print('')
print('~' * 30)
print('')
print(f'{cores["yellow"]}{p18}{cores["close"]} Pessoas maiores de 18')
print(f'{cores["yellow"]}{h_cadas}{cores["close"]} Homens cadastrados')
print(f'{cores["yellow"]}{f20}{cores["close"]} Mulheres com menos de 20 anos')



