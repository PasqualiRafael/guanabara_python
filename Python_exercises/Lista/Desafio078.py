from modulos import pasqualiFinal

pasqualiFinal.ini(f'Input list')

# var
my_list = []
# laço
for valor in range(0, 5):
    num = int(input(f'Type {valor + 1}º value: '))
    my_list.append(num)
print('-' * 40)
print(my_list)
print('-' * 40)
print(f'O maior valor digitado foi: {max(my_list)}')
print(f'O menor valor digitado foi: {min(my_list)}')
print('-' * 40)
for pos, x in enumerate(my_list):
    print(f'O numero {x} está em {pos + 1}º na list!')

pasqualiFinal.close()
