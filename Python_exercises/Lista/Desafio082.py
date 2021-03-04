from modulos import pasqualiFinal

pasqualiFinal.ini(f'Input any value on list')

opt = 'S'
my_list = []
par = []
impar = []
while opt in 'S':
    num = int(input(f'Type one number: \n'))
    my_list.append(num)
    print(my_list)
    print('-' * 40)
    opt = str(input(f'Deseja continuar? [S/N]')).strip().upper()[0]
    print('-' * 40)
    while opt not in 'SN':
        opt = str(input(f'Deseja continuar? [S/N]')).strip().upper()[0]
        print('-' * 40)
for x in my_list:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print(f'Lista: {my_list}')
print(f'Par: {par}')
print(f'Impar: {impar}')
print(f'Fim')

pasqualiFinal.close()
