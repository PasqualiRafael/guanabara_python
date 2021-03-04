name = input(f'Qual seu nome?\n')
age = int(input(f'Qual sua idade\n'))

# age = int(user_age)
cent = 100

time = cent - age
t_age = 2019 + time

# def copies():
#     print(f'{name}, no ano {t_age}, voce tera 100 anos\n')

print('{}, no ano {}, voce tera 100 anos\n'.format(name, t_age))

user_many = int(input(f'Quantas copias desta frase?\n'))

print(user_many * '{}, no ano {}, voce tera 100 anos\n'.format(name, t_age))

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()