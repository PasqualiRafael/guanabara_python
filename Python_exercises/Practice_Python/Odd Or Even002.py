#Odd or Even
print(f'Par ou impar!\n')
print(f'')

#input
user_number = int(input('Digite um numero inteiro: \n'))
#user_number = 15

number: int = (user_number % 2 == 0)
test = (user_number % 2)
if number / 2:
    print('Ele e par!')
else:
    print('Ele e impar!')

if number == True:
    print('ele e Par!')
else:
    print('ele e Impar!')

if user_number % 4 == 0:
    print('Esse numero e multiplo de 4')
else:
    print('Esse numero nao e multiplo de 4')

#Multiplo
print(f'Teste se e divisivel!\n')
print(f'')

user_num = int(input('Diga um numero: '))
user_check = int(input('Diga um divisor: '))

num: int = ((user_number % user_check) == 0)
check: float = (user_number / user_check)
#print(num)
if num == True:
    print('{} e divisivel'.format(check))
else:
    print('{} nao e divisivel'.format(check))

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()
