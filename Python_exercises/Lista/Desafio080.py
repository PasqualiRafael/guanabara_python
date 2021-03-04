from modulos import pasqualiFinal

pasqualiFinal.ini(f'Type 5 valor and register right position without use sorted')

my_list = []
maior = 0
menor = 0
for cont in range(1, 6):
    num = int(input(f'Type one value: '))
    if cont == 1 or num > my_list[-1]:
        my_list.append(num)
    else:
        pos = 0
        while pos < len(my_list):
            if num <= my_list[pos]:
                my_list.insert(pos, num)
                break
            pos += 1

print(my_list)

pasqualiFinal.close()
