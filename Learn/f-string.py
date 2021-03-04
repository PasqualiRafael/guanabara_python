from my_modulos import pasqualiFinal
from my_modulos.colors import cores

pasqualiFinal.ini(f"Teste")

name = "Rafael"


print("Meu nome é {}{}{}".format(cores["blue"], name, cores["close"]))
print("")
print(f'Meu nome é {cores["red"]}{name}{cores["close"]}')

pasqualiFinal.close()
