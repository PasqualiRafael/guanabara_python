#Lista
print(f'Cria uma lista e  conta ate o numero escolhido!\n')
print(f'')
# user_min = 1
# user_max = 10
# user_num = 5
user_min = int(input('Digite um numero positivo!\n'))
user_max = int(input('Digite um numero positivo maior que o anterior!\n'))
user_num = int(input('Digite um numero de {} a {}\n'.format(user_min, user_max)))
my_list = {list for list in range(user_min, user_max) if list <= user_num}
print(my_list)


def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')


close()
