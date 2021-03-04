from datetime import date
from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(" Alistamento do exercito ")

# input
year_nasc = int(input(f"Qual ano você nasceu?\n"))

# var
this_year = date.today().year

# condition
if this_year - year_nasc < 18:
    print(f"Voce ainda irá se alistar")
    print(
        "Daqui {}{} ano{}!".format(
            cores["blue"], (year_nasc + 18) - this_year, cores["close"]
        )
    )
elif this_year - year_nasc > 18:
    print(
        "Passou {}{} anos{}, desde o alistamento!".format(
            cores["blue"], (this_year - 18) - year_nasc, cores["close"]
        )
    )
else:
    print(f"Está na hora de se alistar!")


pasqualiFinal.close()
