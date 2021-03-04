from modulos import pasqualiFinal

pasqualiFinal.ini(f'Ler o nome e mostrar na tela')

#user_name = str(input(f'Qual o seu nome completo?'))
user_name = 'Rafael dos santos Pasquali'
print(user_name.upper())
print(user_name.lower())
print(user_name.capitalize())
print(user_name.split())
print(user_name.replace(' ', ''))
print(len(user_name))
print(user_name[:6])
print(len(user_name) - user_name.count(' '))
print(''.join(user_name))
print(user_name.title())


pasqualiFinal.close()

