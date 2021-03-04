#Desafio04
print(f'Dizer tudo que compoe a palavra!\n')
print(f'')

user_word = input('Digite uma palavra:\n')
user_type = type(user_word)
user_num = user_word.isnumeric()
user_alpha = user_word.isalpha()
user_decimal = user_word.isdecimal()
user_print = user_word.isprintable()
user_upper = user_word.isupper()
user_lower = user_word.islower()

print('O tipo dessa palavra e {}'.format(user_type))

#function
def __num__():
    if(user_num == True):
        x = 'Sim'
        print('Esse palavra e numerica: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra e numerica: {}'.format(x))

def __alpha__():
    if(user_alpha == True):
        x = 'Sim'
        print('Esse palavra e alphanumeric: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra e alphanumeric: {}'.format(x))

def __dec__():
    if(user_decimal == True):
        x = 'Sim'
        print('Esse palavra e um decimal: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra e um decimal: {}'.format(x))

def __pri__():
    if(user_print == True):
        x = 'Sim'
        print('Esse palavra e um printavel: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra e um printavel: {}'.format(x))

def __upp__():
    if(user_upper == True):
        x = 'Sim'
        print('Esse palavra esta em maiusculo: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra esta em maiusculo: {}'.format(x))

def __low__():
    if(user_lower == True):
        x = 'Sim'
        print('Esse palavra esta em minusculo: {}'.format(x))
    else:
        x = 'Nao'
        print('Esse palavra esta em minusculo: {}'.format(x))

#call funcition
__num__()
__alpha__()
__dec__()
__pri__()
__upp__()
__low__()


# def main():
#     global user_word
#     x = input(f'A palavra e um numero ou uma string?\n')
#     while (x.lower() != 'numero' and x.lower() != 'string'):
#         if(x == 'numero'):
#             user_word = int(user_word)
#             call_int()
#         elif(x == 'string'):
#             user_word = str(user_word)
#             call_str()
#         else:
#             x = input(f'Voce precisa digitar, uma das duas opcoes numero ou string\n')
#
# def call_int():
#     if (user_word % 2 == 0):
#         print(f'Ele e par!\n')
#     else:
#         print(f'Ele e impar!\n')
#
# def call_str():
#     if (user_word == user_word.upper()):
#         print(f'E um texto uppercase')
#     else:
#         print(f'Ele esta em lowercase')
#
# main()


def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()
