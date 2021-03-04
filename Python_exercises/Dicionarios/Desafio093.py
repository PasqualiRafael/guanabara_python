
regis = dict()
gol = list()
s = 0
regis['Nome'] = str(input(f'Nome do jogador: ')).capitalize().strip()
regis['Part'] = int(input(f'Quantas partidas jogou: '))
for x in range(0, regis['Part']):
    gol.append(int(input(f'Quantos gols na {x + 1}º partida: ')))
    regis['Gols'] = gol
regis['Total'] = sum(gol)
print('-=' * 30)
print(regis)
print('-=' * 30)
for k, v in regis.items():
    print(f'A key {k} tem value: {v}')
print('-=' * 30)
print(f"O Jogador {regis['Nome']}, jogou {regis['Part']} partidas e marcou: {regis['Total']} gols")



