from modulos import pasqualiFinal

pasqualiFinal.ini('Pares e impares list')

my_list = [[], []]

for x in range(0, 7):
    num = int(input(f'Digite o {x + 1}º valor: '))
    if num % 2 == 0:
        my_list[0].append(num)
    else:
        my_list[1].append(num)

my_list[0].sort()
my_list[1].sort()
print(f'Os valores pares: {my_list[0]}')
print(f'Os valores impares: {my_list[1]}')

pasqualiFinal.close()
# pasqualiFinal.ini('Pares e impares list')
#
# par_list = []
# imp_list = []
# my_list = []
#
# for x in range(0, 7):
#     num = int(input(f'Digite o {x + 1}º valor: '))
#     my_list.append(num)
#
# my_list = sorted(my_list)
# print(my_list)
#
# for c in my_list:
#     if c % 2 == 0:
#         par_list.append(c)
#     else:
#         imp_list.append(c)
#
# par_list = sorted(par_list)
# imp_list = sorted(imp_list)
# my_list.clear()
# my_list = par_list + imp_list
# print(my_list)
#
# pasqualiFinal.close()
