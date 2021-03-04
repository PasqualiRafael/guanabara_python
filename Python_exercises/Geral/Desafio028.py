from modulos import pasqualiFinal
from random import randrange
from time import sleep

pasqualiFinal.ini(f'Adivinhe o numero que o computador escolheu')

# var
npc = randrange(6)
user_num = int(input('Escolha um numero entre 0 e 5\n'))

# function
print('Processando...')
sleep(2)
if user_num == npc:
    print(f'Parabens, voce acertou!')
else:
    print(f'Voce errou!')



pasqualiFinal.close()

