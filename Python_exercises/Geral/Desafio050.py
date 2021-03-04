from modulos import pasqualiFinal

pasqualiFinal.ini('Soma dos pares')

# var
s = 0

# input
for c in range(0, 6):
    x = int(input('Qual o valor a ser somado?\n'))
    if x % 2 == 0:
        s += x
print('')
print('A soma é: {}'.format(s))

pasqualiFinal.close()
