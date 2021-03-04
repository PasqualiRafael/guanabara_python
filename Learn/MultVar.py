from my_modulos import pasqualiFinal
from my_modulos.colors import cores


pasqualiFinal.ini(f'Modo diferente de dar input em variaveis multiplas')


def __one__():
    alu1, alu2, alu3, alu4 = str(input('Digite o nome dos quatro alunos, separados com espaço: ')).split(' ', 3)
    print('O nome do Primeiro aluno: {}'. format(alu1.title()))
    print('O nome do Segundo aluno: {}'. format(alu2.title()))
    print('O nome do Terceiro aluno: {}'. format(alu3.title()))
    print('O nome do Quarto aluno: {}'. format(alu4.title()))


def __two__():
    value = []
    for c in range(0, 4):
        user_n = str(input('Digite o nome dos alunos\n'))
        value.append(user_n)
    print(value)


def __three__():
    alu1234 = list(map(str, input('Digite o nome dos quatro alunos, separados com espaço: ').strip().split()))
    for x in range(0, 3):
        aluno = alu1234[x]
        print(f'O nome do Primeiro aluno: {aluno.title()}')

    # alu1 = alu1234[0]
    # alu2 = alu1234[1]
    # alu3 = alu1234[2]
    # alu4 = alu1234[3]
    # print('O nome do Primeiro aluno: {}'. format(alu1.title()))
    # print('O nome do Segundo aluno: {}'. format(alu2.title()))
    # print('O nome do Terceiro aluno: {}'. format(alu3.title()))
    # print('O nome do Quarto aluno: {}'. format(alu4.title()))


def func(user_num):
    if user_num == 1:
        __one__()
    elif user_num == 2:
        __two__()
    elif user_num == 3:
        __three__()
    else:
        print('Escolha apenas 1 ou 3.')


num = int(input(f'`{cores["bw"]}Escolha o numero 1 ou 3{cores["close"]}\n'))
func(num)

pasqualiFinal.close()
