from modulos import pasqualiFinal

pasqualiFinal.ini(f'Input value on list')

opt = 'S'
my_list = []
while opt in 'S':
    my_list.append(int(input(f'Type any value: ')))
    print('-' * 40)
    opt = str(input(f'Deseja continuar? [S/N]')).strip().upper()[0]
    while opt not in 'SN':
        opt = str(input(f'Deseja continuar? [S/N]')).strip().upper()[0]
    print('-' * 40)

print(f'Foram digitados: {len(my_list)}')
my_list.sort(reverse=True)
print(my_list)
if 5 in my_list:
    print(f'A lista tem o numero 5 ele está na {my_list.index(5)}º posição')
else:
    print(f'O valor 5 não está na lista!')
print(f'Fim')

pasqualiFinal.close()
