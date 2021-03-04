from modulos import pasqualiFinal
from random import randint
from operator import itemgetter

pasqualiFinal.ini('Dados')

placar = {'Jogador 1': randint(1, 6),
          'Jogador 2': randint(1, 6),
          'Jogador 3': randint(1, 6),
          'Jogador 4': randint(1, 6),
          }
print(f'Valores sorteados:')
for k, v in placar.items():
    print(f'O {k} tirou: {v}')
print('-' * 30)
print(f'=== RANK DOS JOGADORES ===')
ranking = list(sorted(placar.items(), key=itemgetter(1), reverse=True))
for k, v in enumerate(ranking):
    print(f'{k + 1}º lugar: {v[0]} com {v[1]}')



pasqualiFinal.close()