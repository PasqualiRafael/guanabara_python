from modulos import pasqualiFinal
from modulos.colors import cores


pasqualiFinal.ini(f' Dicionarios dentro de listas ')

# var
pessoa = list()
women = list()
user = dict()
idade_s = media = c = 0

# laço
while True:
    cont = 'S'
    user.clear()
    user['Nome'] = str(input(f'Digite o nome: ')).strip().capitalize()
    user['idade'] = int(input(f'{user["Nome"]} tem quantos anos: '))
    idade_s += user['idade']

# While Sexo
    while True:
        user['sexo'] = str(input(f'Sexo(H/M): ')).upper().strip()
        if user['sexo'] in 'MH':
            break
        print(f'Digite h ou m.')

    if user['sexo'] == 'M':
        women.append(user.copy())

    pessoa.append(user.copy())

# while Continuar
    while True:
        cont = str(input(f'Deseja continuar? [S/N]')).upper().strip()
        if cont in 'SN':
            break
        print(f'Digite S ou N')

    if cont == 'N':
        break

# calc
media = idade_s / len(pessoa)

# print
print('-=' * 30)
print(f'{cores["red"]}A){cores["close"]} Foram cadastradas: {len(pessoa)} pessoas.')
print(f'{cores["red"]}B){cores["close"]} A média de idade do grupo cadastrado: {media} anos.')
print(f'{cores["red"]}C){cores["close"]} As mulheres são: ', end='')
for x in women:
    print(f'{women[c]["Nome"]}', end=' - ')
    c += 1
print('')
print(f'{cores["red"]}D){cores["close"]} Idade maior que a média: ')
for x in pessoa:
    if x['idade'] >= media:
        print(f'{x["Nome"]} = {x["idade"]} Anos')
print('-=' * 30)


pasqualiFinal.close()



