from modulos import pasqualiFinal

pasqualiFinal.ini('Comparar peso')

# input


# var
value = []

# laço
for c in range(1, 6):
    user_massa = float(input('Qual a massa da {}º pessoa\n'.format(c)))
    value.append(user_massa)

print('O peso mais alto foi {}Kg'.format(max(value)))
print('O peso mais baixo foi {}Kg'.format(min(value)))







pasqualiFinal.close()
