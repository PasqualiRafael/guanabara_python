from modulos import pasqualiFinal

pasqualiFinal.ini('Tabuada')

user_num = int(input('Qual o numero: \n'))

for x in range(0, 21):
    s = x * user_num
    print('{} x {} = {}'.format(x, user_num, s))

pasqualiFinal.close()
