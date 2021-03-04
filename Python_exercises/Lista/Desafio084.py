from modulos import pasqualiFinal

pasqualiFinal.ini(f'lista composta')

group = []
person = []
mai = men = 0
opt = 'S'

while opt in 'S':
    person.append(str(input(f'Qual o nome: ').strip().capitalize()))
    person.append(int(input(f'Qual sua massa: ')))
    if len(group) == 0:
        mai = men = person[1]
    else:
        if person[1] > mai:
            mai = person[1]
        if person[1] < men:
            men = person[1]
    group.append(person[:])
    person.clear()
    opt = str(input(f'Quer continuar? [S/N]')).strip().upper()[0]
    while opt not in 'SN':
        opt = str(input(f'Quer continuar? [S/N]')).strip().upper()[0]


print('-' * 40)
print(f'Quantidade de pessoas cadastradas: {len(group)}')
print(f'O maior peso: {mai}Kg. Peso de ', end='')
for x in group:
    if x[1] == mai:
        print(f'[{x[0]}] ', end='')
print()
print('-' * 40)
print(f'O menor peso: {men}Kg. Peso de ', end='')
for x in group:
    if x[1] == men:
        print(f'[{x[0]}] ', end='')
print()
print('-' * 40)

pasqualiFinal.close()
