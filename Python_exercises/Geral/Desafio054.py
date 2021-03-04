from modulos import pasqualiFinal
from datetime import date

pasqualiFinal.ini("Maioridade")

# var
this_year = date.today().year
s = 0

for x in range(1, 8):
    born_year = int(input("Qual os anos de nascimento da {}º pessoa?\n".format(x)))
    mai = this_year - born_year
    if born_year < this_year:
        if mai < 18:
            s += 1
    else:
        print("Voce precisa colocar um ano de nascimento valido.")

print("{} pessoas ainda não atingiram a maioridade".format(s))

pasqualiFinal.close()
