from modulos import pasqualiFinal

pasqualiFinal.ini(f'Adicionar varios valores na list')

# var
my_list = []

# loop


def _one_():
    while True:
        num = int(input(f'Type one number: \n'))
        print('-' * 40)
        if num not in my_list:
            my_list.append(num)
        else:
            print(f'This value already be add!')
            print('-' * 40)
        print(f'Ordem crescente: ', end='')
        print(sorted(my_list))


def _two_():
    while True:
        num = int(input(f'Type one value: \n'))
        if num not in my_list:
            my_list.append(num)
        else:
            print(f'This value already be add!')
            print('-' * 40)
        print(my_list)
        print('-' * 40)
        opt = ' '
        while opt not in 'SN':
            opt = str(input(f'Deseja continuar? [S/N]')).strip().upper()[0]
        if opt in 'N':
            break
    print(sorted(my_list))
    print(f'FIM')


_two_()

pasqualiFinal.close()
