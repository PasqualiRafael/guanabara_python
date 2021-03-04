from modulos import pasqualiFinal

pasqualiFinal.ini('Carro alugado valor a pagar')

# var
user_km = int(input(f'Quantos km o carro rodou?\n'))
user_day = int(input(f'Quantos dias voce ficou com o carro?\n'))

car = 60
km: float = 0.15

# cal
cost = (car * user_day) + (km * user_km)

# function


def __car__(u_km, u_d):
    print('O carro foi usado por {} dia, rodou {} km | o custo será de R${:.2f}'.format(u_d, u_km, cost))


__car__(user_km, user_day)


pasqualiFinal.close()

