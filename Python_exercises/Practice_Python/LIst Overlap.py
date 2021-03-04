from modulos import pasqualiFinal
from random import randrange

pasqualiFinal.ini('List Overlap')

# ar
my_list_a = []
my_list_b = []
my_comm = []
my_range = randrange(1, 10)

# laço
for c in range(0, my_range):
    my_list_a.append(randrange(0, 10))
    my_list_b.append(randrange(0, 10))

# laço
for x in my_list_a: # verificando os numeros que tem na lista a
    if x in my_list_b: # verificando se tem o numero na lista b
        my_comm.append(x) # adicionando os numeros em comum


# print
print(my_list_a)
print(my_list_b)
print(my_comm)


pasqualiFinal.close()

