from modulos import pasqualiFinal

pasqualiFinal.ini(f'Tabuada')

user_n = int(input('Escolha um numero: \n'))
_tab = list(range(11))

for y in _tab:
    print(int(_tab[y]) * user_n)



pasqualiFinal.close()

