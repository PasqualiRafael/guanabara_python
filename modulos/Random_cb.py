#import
from modulos import pasqualiFinal
from math import ceil, floor
from random import uniform

# Title
pasqualiFinal.ini(f'Inteiro mais Proximo pra cima e baixo')


def random_close(min_floor, max_ceil):
    user_num = uniform(min_floor, max_ceil)

    #print
    print('{:.2f}'.format(user_num))
    num = ceil(user_num)
    print('O numero mais proximo de {:.2f} para cima é: {}'.format(user_num, num))
    num = floor(user_num)
    print('O numero mais proximo de {:.2f} para baixo é: {}'.format(user_num, num))

#var
user_num = uniform(1, 100)

#print
print('{:.2f}'.format(user_num))
num = ceil(user_num)
print('O numero mais proximo de {:.2f} para cima é: {}'.format(user_num, num))
num = floor(user_num)
print('O numero mais proximo de {:.2f} para baixo é: {}'.format(user_num, num))

# Close
pasqualiFinal.close()
