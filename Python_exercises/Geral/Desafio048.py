from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Soma entre impares multiplos de 3')

# var
s = 0

# laço
for x in range(1, 500):
    if x % 2 == 1 and x % 3 == 0:
        s += x

print('A soma de todos numeros impares\nmultiplo de 3 é: {}{}{}'.format(cores['green'], s, cores['close']))
print('Fim')

pasqualiFinal.close()
