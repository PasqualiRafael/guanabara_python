from modulos import pasqualiFinal
from modulos.colors import cores
from time import sleep

pasqualiFinal.ini(" Contagem regressiva para fogos ")

# laço
for x in range(10, 0, -1):
    print('{:^36}'.format(x))
    sleep(1)
msg = "Feliz Ano Novo"
print("{:^36}".format(msg))

pasqualiFinal.close()
