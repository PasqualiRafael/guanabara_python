'''
\033[0;33;44m
0 = style
33 = text
44 = background

# style
0 = none(default)
1 = bold(negrito)
4 = underline
7 = negative

# text
30 = white
31 = red
32 = green
33 = yellow
34 = blue
35 = purple
36 = azul claro
37 = cinza

# backgroung
40 = white
41 = red
42 = green
43 = yellow
44 = blue
45 = purple
46 = azul claro
47 = cinza
'''

# var
nome = 'Rafael'

# dicionary
cores = {'close': '\033[m', 'red': '\033[31m'}

# testes
print(' ')
print('\033[0;32mQual o comprimento da primeira reta?\033[m\n')
print('\033[7;34;40mQual o comprimento da primeira reta?\033[m\n')
print('\033[7;33;40m' + 'Qual o comprimento da primeira reta?' + '\033[m' + '\n')
print('\033[7;32;40m' + 'Qual o comprimento da primeira reta?' + '\033[m\n')
print('Bom dia, {}{}{}!!!'.format('\033[31m', nome, '\033[m'))
print('Bom dia, {}{}{}!!!'.format(cores['red'], nome, cores['close']))
print(' ')

# font
print('\033[0mDefault\033[m 0')
print('\033[1mNegrito\033[m 1')
print('\033[4mUnderLine\033[m 4')
print('\033[7mNegative\033[m 7')
print('')

# backfground
print('\033[40m' + (' ' * 12) + '\033[m 40')
print('\033[41m' + (' ' * 12) + '\033[m 41')
print('\033[42m' + (' ' * 12) + '\033[m 42')
print('\033[43m' + (' ' * 12) + '\033[m 43')
print('\033[44m' + (' ' * 12) + '\033[m 44')
print('\033[45m' + (' ' * 12) + '\033[m 45')
print('\033[46m' + (' ' * 12) + '\033[m 46')
print('\033[47m' + (' ' * 12) + '\033[m 47')
print(' ')
# text
print('\033[30m' + ('a' * 12) + '\033[m 30')
print('\033[31m' + ('a' * 12) + '\033[m 31')
print('\033[32m' + ('a' * 12) + '\033[m 32')
print('\033[33m' + ('a' * 12) + '\033[m 33')
print('\033[34m' + ('a' * 12) + '\033[m 34')
print('\033[35m' + ('a' * 12) + '\033[m 35')
print('\033[36m' + ('a' * 12) + '\033[m 36')
print('\033[37m' + ('a' * 12) + '\033[m 37')
print(' ')


