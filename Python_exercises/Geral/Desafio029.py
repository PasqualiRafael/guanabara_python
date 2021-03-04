from modulos import pasqualiFinal

pasqualiFinal.ini(f'Sistema de multa')

# var
user_car = int(input(f'Qual a velocidade em km do carro que passou?\n'))
cost_km = 7

# cal
ticket = (user_car - 80) * cost_km

# func
if user_car > 80:
    print('Você foi multado, receberá uma multa no valor de R$ {:.2f}'.format(ticket))
else:
    print(f'Você está dentro do limite de velocidade!')


pasqualiFinal.close()

