from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Palindromo')

# input
frase = str(input('Escreva uma frase e direi se é um palindromo:\n')).lower()
# frase = 'anotaram a data da maratona'.lower()

# trans
cal = frase.strip().split()
trans_frase = ''.join(cal)

# condition
if trans_frase == trans_frase[::-1]:
    print('A frase:\n{}{}{}\nÉ um Palindromo'.format(cores['blue'], frase, cores['close']))
    print('A frase: {}{}{}'.format(cores['blue'], trans_frase[::-1], cores['close']))
else:
    print('Está frase {}não{} é um Palindromo'.format(cores['red'], cores['close']))
    print('A frase: {}{}{}'.format(cores['blue'], trans_frase[::-1], cores['close']))
pasqualiFinal.close()
