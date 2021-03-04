from modulos import pasqualiFinal
from modulos.colors import font, cores
from time import sleep

pasqualiFinal.ini(f'Emprestimos bancarios')

# input
house = float(input(f'Qual o valor da casa?\n'))
salario = float(input(f'Qual seu salario?\n'))
years = int(input(f'Em quantos anos voce irá pagar?\n'))

print('')
print('{}Processando...{}'.format(cores['blue'], cores['close']))
print('')
sleep(3)

# cal
month = years * 12
v_men = house / month
minimo = salario * 30 / 100


# condition
if v_men <= minimo:
    print('Empréstimo {}{}ACEITO{}! A prestação é: {:.2f}'.format(font['bold'], cores['green'], cores['close'], v_men))
else:
    print('Seu empréstimo foi {}{}NEGADO{}! A prestação é: {:.2f} o seu minimo é: {}'.format(font['bold'], cores['red'], cores['close'], v_men, minimo))

pasqualiFinal.close()
