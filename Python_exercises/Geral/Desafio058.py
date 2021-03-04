from modulos import pasqualiFinal
from random import randint
from modulos.colors import cores


pasqualiFinal.ini('Jogo do pensar')

# var
pc = randint(0, 10)
user_num: int = 0
palpites = 0

# laço
while user_num != pc:
    print('')
    user_num = int(input('Adivinhe qual numero entre {}0 e 10{}, o computador pensou?\n'.format(cores['yellow'], cores['close'])))
    if user_num > 10:
        print('Voce precisa escolher um numero entre {}0 e 10{}'.format(cores['yellow'], cores['close']))
        print('')
    elif user_num != pc:
        if user_num > pc:
            print('Menos!!!')
        elif user_num < pc:
            print('Mais!!!')
        print('{}Voce errou, tente novamente!{}'.format(cores['red'], cores['close']))
        palpites += 1

print('{}Voce acertou!{} Com apenas {}{} palpites{}'.format(cores['green'], cores['close'], cores['yellow'], palpites, cores['close']))


pasqualiFinal.close()
