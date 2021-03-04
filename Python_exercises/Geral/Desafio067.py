from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Tabuada de qualquer numero solicitado')

n = result = cont = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor?\n'))
    print('~' * 20)
    if n < 0:
        break
    while cont <= 10:
        result = cont * n
        print(f'{cont} x {n} = {result}')
        cont += 1
    cont = 0
    print('~' * 20)


print(f'Fim')

pasqualiFinal.close()
