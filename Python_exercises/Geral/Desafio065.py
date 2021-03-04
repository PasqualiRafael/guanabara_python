from modulos import pasqualiFinal

pasqualiFinal.ini('Media, max e min')

resp = ''
nota = 0
media = 0
cont = 0
my_list = []

while resp != 'N':
    cont += 1
    b = media
    nota = int(input('Qual a nota: '))
    my_list.append(nota)
    media = (nota + b) / cont
    resp = str(input('Deseja continuar? [S/N]\n')).upper().strip()[0]
    if resp not in 'SN':
        print('Voce precisa digitar uma das opções.')
        resp = str(input('Deseja continuar? [S/N]\n')).upper().strip()[0]

print(my_list)
print(max(my_list), min(my_list))
print(media)


pasqualiFinal.close()
