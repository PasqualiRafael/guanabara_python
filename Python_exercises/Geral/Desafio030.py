from modulos import pasqualiFinal

pasqualiFinal.ini(f'Par ou Impar')

# var
user_num = int(input('Escolha um numero:\n'))

# cal
if user_num % 2 == 0:
    print(f'Ele é Par')
else:
    print(f'Ele é Impar')

pasqualiFinal.close()
