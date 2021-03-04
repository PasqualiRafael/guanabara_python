#Desafio09
print(f'Conversor de temperatura!\n')
print(f'')

#import

#input
user_choose = float(input('Digite o numero de celsius: \n'))

#var


#cal
temp_fahr = (user_choose * 1.8) + 32
#temp_cel = (fahr - 32) / 1.8

#Print
print('A temperatura {} em Celcius, é o mesmo que {} em Fahrenheit'.format(user_choose, temp_fahr))

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()