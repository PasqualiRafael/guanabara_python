#Desafio10
print(f'Transformar dollar em real!\n')
print(f'')
#import


#input
user_dolar = float(input(f'Quantos dolares voce tem?\n'))

#variables
dollar: float = 3.27
real = user_dolar / dollar

#print
print('Voce tem {} reais'.format(real))

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()