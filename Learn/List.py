from my_modulos import pasqualiFinal

pasqualiFinal.ini(f'Lists')

my_list = ['hamburguer', 'refri', 'picole', 'pudim']


def _one_():  # adiciona um valor
    my_list.append('cookie')


def _two_():  # insere um valor na posicao especificada
    my_list.insert(0, 'bolo')


def _three_():
    del my_list[2]  # removerá o elemento e reorganizara os indices
    # my_list.remove('picole')  # removerá o elemento e reorganizara os indices
    # my_list.pop()  # removerá o ultimo elemento e reorganizara os indices
    # my_list.pop(2)  # removerá o elemento especificado e reorganizara os indices


def _four_():
    a = [2, 3, 4, 7]
    #  b = a  # Isso faz com que o a fique connectado ao b, todos os valores alterados em b, tambem mudará A
    b = a[:]  # Dessa forma voce criará uma copia perfeita da lista a, sem conecao
    b[2] = 8
    print(f'Lista A: {a}')
    print(f'Lista B: {b}')


# variavel[x].sort() para organizar


def func(user_num):
    if user_num == 1:
        _one_()
    elif user_num == 2:
        _two_()
    elif user_num == 3:
        _three_()
    else:
        _four_()


num = int(input(f'Escolha a função de 1 á 4: '))
func(num)

print('-' * 40)
'''
for c in range(0, len(my_list)):
    print(f'{my_list[c]} está em: {c}')
'''
for pos, x in enumerate(my_list):
    print(f'Na {pos + 1}º posição está: {x.upper()}')
