from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f" Nome e preço ilimitado ")

# var
name: str = ""
cost: float = 0
cont: str = ""
quant: int = 0
soma: float = 0
many_more: int = 0
menor_name: str = ""
menor_cost: float = 0

# laço
while True:
    name = str(input("Nome do produto: ")).capitalize().strip()
    cost = float(input("Valor do produto: R$"))
    quant += 1

    if quant == 1:
        menor_cost = cost
        menor_name = name
    else:
        if cost < menor_cost:
            menor_name = name
            menor_cost = cost

    while cost < 0:
        print("Coloque um valor positivo!")
        cost = float(input("Valor do produto: R$"))
        print("")

    # cal de cost
    if cost >= 1000:
        many_more += 1

    soma += cost

    cont = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    print("")

    while cont not in "SN":
        print("Escolha uma das opções!")
        cont = str(input("Deseja continuar? [S/N]"))
        print("")

    if cont in "N":
        break

print(f'Foram gastos {cores["yellow"]}R${soma:.2f}{cores["close"]}')
print(
    f'{cores["yellow"]}{many_more}{cores["close"]} Custam mais de {cores["yellow"]}R$1000,00{cores["close"]}'
)
print(
    "O produto mais barato é: {}{}{} por {}R${:.2f}{}".format(
        cores["yellow"],
        menor_name,
        cores["close"],
        cores["yellow"],
        menor_cost,
        cores["close"],
    )
)
