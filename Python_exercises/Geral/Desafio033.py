from modulos import pasqualiFinal


pasqualiFinal.ini(f"Ler tres numeros e mostrar o maior e menor")

# var
n1 = int(input("Primeiro numero:\n"))
n2 = int(input("Segundo numero:\n"))
n3 = int(input("Terceiro numero:\n"))

_maior = n1
_menor = n2

# verificar maior
if n2 > n1 and n2 > n3:
    _maior = n2
if n3 > n2 and n3 > n1:
    _maior = n3
# verificar menor
if n1 < n2 and n1 < n3:
    _menor = n1
if n3 < n1 and n3 < n2:
    _menor = n3
print('O menor numero é: {}'.format(_menor))
print('O maior numero é: {}'.format(_maior))

# if n1 > n2 and n1 > n3:
#     print("O maior é: {}".format(n1))
# elif n1 < n2 and n1 < n3:
#     print("O menor é: {}".format(n1))
# if n2 > n1 and n2 > n3:
#     print("O maior é: {}".format(n2))
# elif n2 < n1 and n2 < n3:
#     print("O menor é: {}".format(n2))
# if n3 > n1 and n3 > n2:
#     print("O maior é: {}".format(n3))
# else:
#     print("O menor é: {}".format(n3))


pasqualiFinal.close()
