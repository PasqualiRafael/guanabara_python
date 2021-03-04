from modulos import pasqualiFinal

pasqualiFinal.ini(f'Listagem de preços')

my_tuples = (
    "Lápis",
    1.75,
    "Borracha",
    2,
    "Caderno",
    15.90,
    "Estojo",
    25,
    "Transferidor",
    4.2,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Canetas",
    22.3,
    "Livro",
    34.9,
)
print('-' * 40)
print(f'{"Listagem de Preço":^40}')
print('-' * 40)
for pos in range(0, len(my_tuples)):
    if pos % 2 == 0:
        print(f'{my_tuples[pos]:.<30}', end='')
    else:
        print(f'R${my_tuples[pos]:>7.2f}')
print('-' * 40)

pasqualiFinal.close()
