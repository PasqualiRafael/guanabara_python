from modulos import pasqualiFinal

pasqualiFinal.ini('List Comprehensions')

# var
my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
my_oldlist =[]

# laço
for c in my_list:
    if c % 2 == 0:
        my_oldlist.append(c)


print(my_oldlist)
pasqualiFinal.close()
