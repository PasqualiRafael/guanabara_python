from modulos import pasqualiFinal
from random import randint

pasqualiFinal.ini(f'listagem de numeros')

# var
turple = (randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4), randint(0, 4))

print(turple)

print(f'Max: {max(turple)}\nMin: {min(turple)}')

