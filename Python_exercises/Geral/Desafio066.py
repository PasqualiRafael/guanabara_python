from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini(f'Criar um programa que de break')

s = n = cont = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A quantidade de numeros digitados foi: {cores["blue"]}{cont}{cores["close"]}')
print(f'A soma dos numeros é: {cores["blue"]}{s}{cores["close"]}')

pasqualiFinal.close()
