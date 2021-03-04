from modulos import pasqualiFinal
from modulos.colors import cores
from datetime import date

pasqualiFinal.ini(f'Natação categoria de acordo com a idade')

# input
born = int(input(f'Digite a data de nascimento:\n'))

# var
year = date.today().year

# calc
age = year - born

if age < 9:
    print('Sua categoria é: {}Mirim{}'.format(cores['blue'], cores['close']))
elif 9 <= age < 14:
    print('Sua categoria é: {}Infantil{}'.format(cores['blue'], cores['close']))
elif 14 <= age < 19:
    print('Sua categoria é: {}Junior{}'.format(cores['blue'], cores['close']))
elif 19 <= age < 20:
    print('Sua categoria é: {}Senior{}'.format(cores['blue'], cores['close']))
else:
    print('Sua categoria é: {}Master{}'.format(cores['blue'], cores['close']))


pasqualiFinal.close()
