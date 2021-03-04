from modulos import pasqualiFinal

pasqualiFinal.ini(f'Expressão matematica')

exp = list(input(f'Digite uma expressão matematica: '))
#exp = ['(', '3', '+', '4', ')']
print(exp)
cont = exp.count('(')
contclose = exp.count(')')

if cont == contclose:
    if exp.index('(') < exp.index(')'):
        print(f'Sua expressão é valida!')
    else:
        print(f'Sua expressão não é valida!')
else:
    print(f'Sua expressão não é valida!')


pasqualiFinal.close()
