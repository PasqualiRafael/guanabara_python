#Desafio05
user_num = int(input(f'Digite um numero:\n'))
print(f'')


num_min = user_num - 1
num_max = user_num + 1

print('O numero antecessor e: {}'.format(num_min))
print('O numero sucessor e: {}'.format(num_max))

#Desafio06
double = user_num * 2
triple = user_num * 3
quad = user_num ** 2
_raiz = user_num ** (1 / 2)

print('Seu dobro e: {}'.format(double))
print('Seu triplo e: {}'.format(triple))
print('O quadrado de {} e: {}'.format(user_num, quad))
print('Sua raiz e: {:.3f}'.format(_raiz))

#Desafio07
user_n1 = float(input(f'Qual sua primeira nota?\n'))
user_n2 = float(input(f'Qual sua segunda nota?\n'))

media = (user_n1 + user_n2) / 2
print('Sua media e: {}'.format(media))

#Desafio08
user_m = float(input(f'Quantos metros?\n'))
cm = user_m * 100
mm = user_m * 1000
print('{} metros e o mesmo que {} centimetros'.format(user_m, cm))
print('{} metros e o mesmo que {} milimetros'.format(user_m, mm))

# user_choose = str(input('Escolha se deseja colocar o numero em "m" ou "cm":\n'))
# user_m = float(input(f'Numero:\n'))
# cm = user_m * 100
# m = user_m / 100
# x = user_choose
#
# while(x.lower() != 'm' and x.lower() != 'cm'):
#     print('Voce precisa escolher "m" ou "cm"')
#     if(x == 'm'):
#         print('{} metros e o mesmo que {} centimetros'.format(user_m, cm))
#
#     else:
#         print('{} centimetros e o mesmo que {} metros'.format(user_m, m))
# else:
#     user_choose = str(input('Escolha se deseja colocar o numero em "m" ou "cm":\n'))

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()