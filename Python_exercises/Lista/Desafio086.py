from modulos import pasqualiFinal

pasqualiFinal.ini(f'Matriz')


matriz = [[], [], []]
num = soma = soma_b = 0

for c in range(0, 9):
    num = int(input(f'Qual o {c + 1} valor: '))
    if num % 2 == 0:
        soma += num
    if c < 3:
        matriz[0].append(num)
    if 3 <= c < 6:
        matriz[1].append(num)
    if 6 <= c < 9:
        matriz[2].append(num)

c = 2
for l in range(0, 3):
    soma_b += matriz[l][c]

print('-' * 40)
print(f'[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]')
print('-' * 40)
print(f'A soma dos valores pares são: {soma}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
print(f'A soma dos valores da terceira linha são: {soma_b}')



'''
matriz = [[0, 0, 0 ], [0, 0, 0], 0, 0, 0]]

for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end= '')
    print()
'''



