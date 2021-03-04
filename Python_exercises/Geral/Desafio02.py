from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Apresentação')

user_name = str(input(f'Qual seu nome?\n'))
print(f'Seja bem vindo, {cores["red"]}{user_name.capitalize()}{cores["close"]}')


pasqualiFinal.close()
