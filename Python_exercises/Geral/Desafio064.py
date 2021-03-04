from modulos import pasqualiFinal

pasqualiFinal.ini("Ler e broke")

cont = 0
result = 0
num = 0

while num != 999:
    cont += 1
    b = result
    num = int(input("Digite um valor no teclado: "))
    result = num + b

print('Voce digitou {} valores'.format(cont - 1))
print('A soma de todos os valores foi: {}'.format(result - 999))

pasqualiFinal.close()
