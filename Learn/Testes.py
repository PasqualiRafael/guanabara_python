############################

name: str = input(f'whats your name?\n')
print(name)


def greeting(user_name):
    print(f'hi, {user_name.capitalize()}')


greeting(name)

# ternary
age = 21

if age >= 21:
    old_enough = True
else:
    old_enough = False

old_enough = True if age >= 21 else False

############################

#############################
# list
# iniatialize
my_list = [1, 2, 3, 'test', True, 4.5, 88]

# add item

# acess item
print(my_list[3])

# change item
my_list[3] = 'Mudei'
print(my_list[3])

# remove item from index
del my_list[3]
print(my_list)

# iterate
for item in my_list:
    print(item)

############################

############################

# Ainda não aprendi a mexer em for e while

user_choose = str(input('Escolha se deseja colocar o numero em "m" ou "cm":\n'))
x = user_choose

while x.lower() != 'm' and x.lower() != 'cm':
    print(f'Escolha uma das duas medidas m ou cm')
    x = str(input(f'Escolha se deseja colocar a medida em m ou cm: \n'))

user_m = float(input(f'Numero:\n'))
cm = user_m * 100
m = user_m / 100

if x == 'm':
    print(f'{m} metros e o mesmo que {cm} centimetros')

else:
    print(f'{cm} centimetros e o mesmo que {m} metros')

    # Tentativa de tabuada

    ############################

    if quant == 1:
        menor_cost = cost
        menor_name = name
    else:
        if cost < menor_cost:
            menor_name = name
            menor_cost = cost

    # se ambas premissas acima forem verdadeiras podemos usar o 'or'

    if quant == 1 or cost < menor_cost:  # se um ou outro for verdadeiro execurá o codigo
        menor_cost = cost
        menor_name = name
