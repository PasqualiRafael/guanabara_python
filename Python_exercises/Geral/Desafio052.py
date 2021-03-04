from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Numeros Primos')

# input
user_pri = int(input('Digite um numero:\n'))


def __one__(primo):
    for x in range(2, primo + 1):
        if x != primo:
            if primo % x == 0:
                print('Ele não é primo')
                break
        else:
            print('Ele é primo')
    print('Fim')


__one__(user_pri)

pasqualiFinal.close()
