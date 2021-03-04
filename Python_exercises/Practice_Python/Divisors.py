from modulos import pasqualiFinal

pasqualiFinal.ini(f"Divisores")

# input
user_div = int(input("Qual o divisor?\n"))
user_lim = int(input("testar até qual numero?\n"))
print("\n")

# var
my_quoc = []
my_resul = []
cont = 0

# laço
for c in range(0, user_lim + 1):
    if c % user_div == 0:
        cont += 1
        resul = c // user_div
        my_resul.append(resul)
        my_quoc.append(c)
print("Os numeros divisiveis por {} são: ".format(user_div))
for x in range(0, cont):
    print("{} / {} = {}".format(my_quoc[x], user_div, my_resul[x]))


pasqualiFinal.close()
