from modulos import pasqualiFinal
from modulos.colors import cores
from random import randrange

pasqualiFinal.ini(f' Mega Sena ')

my_list = list()
user_games = int(input(f'{cores["red"]}Quantos jogos deseja fazer?{cores["close"]}\n'))


def luck(num):
    for x in range(0, num):
        for c in range(0, 6):
            def again():
                lim = randrange(1, 61)
                if lim not in my_list:
                    my_list.append(lim)
                else:
                    again()
            again()

        my_list.sort()
        print(f'Jogo {x + 1}: {my_list}')
        my_list.clear()


luck(user_games)


pasqualiFinal.close()

