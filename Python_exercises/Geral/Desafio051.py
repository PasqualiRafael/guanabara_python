from modulos import pasqualiFinal

pasqualiFinal.ini('Progressão Aritimetica')

# input
term = int(input('Primeiro termo:\n'))
raz = int(input('Razao:\n'))

# var
pa = 0

for c in range(0, 10):
    pa = term + raz
    print('{} + {} = {} '.format(term, raz, pa))
    term += raz

pasqualiFinal.close()
