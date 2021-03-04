from modulos import pasqualiFinal
from math import hypot

pasqualiFinal.ini('Hipotenusa')

# var
user_h = float(input(f'Qual a altura?\n'))
user_l = float(input(f'Qual o comprimento?\n'))

# cal
user_hypo = hypot(user_l, user_h)

# Print
print('A altura: {} | Comprimento: {} | A hipotenusa: {:.2f}'.format(user_h, user_l, user_hypo))

pasqualiFinal.close()

