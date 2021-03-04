from modulos import pasqualiFinal

pasqualiFinal.ini(f' Caixa Eletronico')

withdrawn: int = 0
total: int = 0
ced: int = 50
totced: int = 0


withdrawn = int(input('Qual valor a ser sacado: R$'))
total = withdrawn

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


print('Fim')

pasqualiFinal.close()
