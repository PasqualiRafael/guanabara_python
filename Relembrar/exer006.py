from math import sqrt

user_n = int(input(f'Digite um numero:\n'))
double = 2 * user_n
triple = 3 * user_n
raiz = user_n ** ( 1 / 2 )
_raiz_ = sqrt(user_n)

print('O dobro: {}'.format(double))
print('O triplo: {}'.format(triple))
print('A raiz Quadrada: {:.2f}'.format(raiz))
print('A raiz Quadrada: {:.2f}'.format(_raiz_))

