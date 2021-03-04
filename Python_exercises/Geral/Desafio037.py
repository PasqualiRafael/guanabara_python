from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini("Conversor de número")

# input
user_num = int(input(f"Escolha um numero:\n"))
base = int(
    input(
        f"Escreva o numero da opção:\n"
        + "{}1{} = binário\n".format(cores["blue"], cores["close"])
        + "{}2{} = octal\n".format(cores["blue"], cores["close"])
        + "{}3{} = hexadecimal\n".format(cores["blue"], cores["close"])
    )
)
print("")

# condition
if base == 1:
    print(
        "O numero em binario é: "
        + "{}".format(cores["yellow"])
        + "{0:b}".format(user_num)
        + "{}".format(cores["close"])
    )
elif base == 2:
    print("O numero em octal é: \033[33m{0:o}\033[m".format(user_num))
elif base == 3:
    print("O numero em hexadecimal é: \033[33m{}\033[m".format(hex(user_num)[2:]))
else:
    print("Escolha uma das {}Opções{}.".format(cores["red"], cores["close"]))

pasqualiFinal.close()
""" Maneiras diferentes de representar o numero em hexadecimal, usando dentro do {0:} b,o,x ou usando
 os comandos bin(),oct() e hex()"""
