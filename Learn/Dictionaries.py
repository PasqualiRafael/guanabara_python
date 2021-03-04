from modulos import pasqualiFinal

pasqualiFinal.ini(' Dictionaries')

# initialize
my_dict = {}

# add item
my_dict['name'] = 'Rafael'
my_dict['state'] = 'SP'
my_dict['age'] = 29

print(my_dict)

# access item
print(my_dict['name'])

# change item
my_dict['name'] = 'Nanda'
my_dict['age'] = '26'

# remove item by index
del my_dict['state']

print(my_dict)

# iterate
for k, v in my_dict.items():
    print(k, '=>', v)

pasqualiFinal.close()
