#Desafio11
print(f'Area e quantidade de tinta!\n')
print(f'')
#input
user_h = float(input('Qual a altura da parede em metros?\n'))
user_l = float(input('Qual a largura da parede em metros?\n'))

_area = user_h * user_l
print('A area desta parede e {}'.format(_area))
print(f'Cada litro de tinta equivale a 2m²')
litro = _area / 2
print('Essa parede de {} m², ira precisar de {} litros de tinta'.format(_area, litro))


def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()