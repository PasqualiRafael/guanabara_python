from modulos import pasqualiFinal
from random import choice

pasqualiFinal.ini(f'Escolher um dos alunos')


def choice_nome(my_lyst):
    user_lyst = list(my_lyst)

    user_lyst.append(str(input(f'Qual o nome do primeiro aluno: \n')))
    user_lyst.append(str(input(f'Qual o nome do segundo aluno: \n')))
    user_lyst.append(str(input(f'Qual o nome do terceiro aluno: \n')))
    user_lyst.append(str(input(f'Qual o nome do quarto aluno: \n')))

    print('O aluno escolhido foi: {}'.format(choice(user_lyst)))


minha_lista = []
choice_nome(minha_lista)

pasqualiFinal.close()
