#Desafio09 Tabuada
print(f'Tabuada!\n')
print(f'')
user_num = int(input('Escolha um numero:\n'))
x = 0
print('-' * 12)


while x <= 20:
    total = x * user_num
    print('{} x {} = {}'.format(x, user_num, total))
    x = x + 1
print('-' * 12)


def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()
