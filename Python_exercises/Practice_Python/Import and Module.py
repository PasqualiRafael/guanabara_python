#Exercicio de import


#import
from math import sqrt
from modulos import pasqualiFinal

pasqualiFinal.ini(f'Aprendendo import and module')

#input
user_num = int(input(f'Escolha um numero: \n'))

#var
raiz = sqrt(user_num)


print('A raiz de {} é: {:.4f}'.format(user_num, raiz))

pasqualiFinal.close()
