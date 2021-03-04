from modulos import pasqualiFinal
from random import choice, shuffle

pasqualiFinal.ini(f'Sorteio de nome')

# var
user_listname = ['Rafael', 'Nanda', 'Quezia', 'Naty']

# cal
user_choice = choice(user_listname)

# print
print(user_choice)
shuffle(user_listname)
print(user_listname)

pasqualiFinal.close()

