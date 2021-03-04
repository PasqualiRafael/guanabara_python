from modulos import pasqualiFinal

pasqualiFinal.ini('Sequencia de Fibonacci')

num = int(input('Digite o primeiro numero: '))
print('')
ant_num = 0
result = 0
cont = 0

while cont < 10:
    result = num + ant_num
    cont += 1
    print('{} + {} = {}'.format(ant_num, num, result))
    num = ant_num
    ant_num = result

pasqualiFinal.close()
