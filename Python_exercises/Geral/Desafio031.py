from modulos import pasqualiFinal

pasqualiFinal.ini(f'Preço da passagem por km')

# var
user_num = int(input('Qual a distancia da viagem?\n'))
_min: float = 0.5
_max: float = 0.45

if user_num <= 200:
    print('Sua viagem custará: R$ {:.2f}'.format(user_num * _min))
else:
    print('Sua viagem custará: R$ {:.2f}'.format(user_num * _max))



pasqualiFinal.close()

