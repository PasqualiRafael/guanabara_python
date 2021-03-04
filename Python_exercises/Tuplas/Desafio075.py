from modulos import pasqualiFinal

pasqualiFinal.ini(f'Guardar em um tupla')

num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: '))
       )
print(f'Voce digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares são: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')


pasqualiFinal.close()
