from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f"Calcular valor a ser pago, e condição de pagamento")

# input
cost_n = float(input("Qual o preço do produto?\n"))
opt = int(
    input(
        f"Escolha o numero de acordo com a forma de pagamento: \n"
        + "{}1{} = Dinheiro ou cheque\n".format(cores["blue"], cores["close"])
        + "{}2{} = à vista no cartão\n".format(cores["blue"], cores["close"])
        + "{}3{} = em até 2x no cartão\n".format(cores["blue"], cores["close"])
        + "{}4{} = 3x ou mais no cartão\n".format(cores["blue"], cores["close"])
    )
)

# var
"""cost_n = 1000"""
v_dinh = cost_n - (cost_n * 10 / 100)
v_cart = cost_n - (cost_n * 5 / 100)
parc_2x = cost_n
parc_3x = cost_n + (cost_n * 20 / 100)

# condition
if opt == 1:
    print(
        "O produto custará: {}{:.2f}{}".format(cores["green"], v_dinh, cores["close"])
    )
elif opt == 2:
    print(
        "O produto custará: {}{:.2f}{}".format(cores["green"], v_cart, cores["close"])
    )
elif opt == 3:
    print(
        "O produto custará: {}{:.2f}{}".format(cores["green"], parc_2x, cores["close"])
    )
elif opt == 4:
    print(
        "O produto custará: {}{:.2f}{}".format(cores["green"], parc_3x, cores["close"])
    )
else:
    print(
        "{}ERRO!{}, Selecione uma das opções validas.".format(
            cores["red"], cores["close"]
        )
    )


pasqualiFinal.close()
