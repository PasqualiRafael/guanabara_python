def __um__():
    for c in range(0, 6):
        print('oi')
    print('fim')


def __dois__():
    for c in range(0, 6):
        print(c)
    print('fim')


def __tres__():
    for x in range(7, -1, -1):
        print(x)
    print('fim')


def __quatro__():
    i = int(input('Qual casa de inicio?'))
    f = int(input('Qual casa de fim?'))
    p = int(input('Qual casa de pulo?'))
    if p == 0:
        print('Escolha um valor de pulo, diferente de Zero\n')
        __quatro__()
    else:
        for c in range(i, f + 1, p):
            print(c)
        print('fim')


def __cinco__():
    s = 0
    for c in range(0, 5):
        n = int(input('Qual o valor? '))
        s += n
    print('A soma dos valores colocados é: {}'.format(s))


def func(user_num):
    if user_num == 1:
        __um__()
    elif user_num == 2:
        __dois__()
    elif user_num == 3:
        __tres__()
    elif user_num == 4:
        __quatro__()
    elif user_num == 5:
        __cinco__()
    else:
        num = int(input('Escolha um numero entro 1 e 5\n'))
        func(num)


num = int(input(f'Escolha a função de 1 á 5: '))

func(num)