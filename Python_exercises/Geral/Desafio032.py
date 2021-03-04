from modulos import pasqualiFinal
from datetime import date

pasqualiFinal.ini(f'Mostre se é ano bissexto')

# var
#user_year = int(input(f'Digite um ano:\n'))
user_year = 2000

# function
if user_year == 0:
    user_year = date.today().year
    print(user_year)
elif user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
    print(f'Esse ano foi bissexto')
else:
    print(f'Esse ano não foi bissexto')


pasqualiFinal.close()

