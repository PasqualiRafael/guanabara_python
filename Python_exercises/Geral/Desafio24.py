from modulos import pasqualiFinal

pasqualiFinal.ini(f'Digite uma cidade e verifique se começa com a palavra SANTO')

# input
user_city = str.upper(input('Digite um nome de uma cidade: ')).strip()

# var
x = bool(user_city[:5].find('SANTO'))


# function
if x == False:
    print(f'A palavra Santo está no começo')
else:
    print(f'Não começa com a palavra Santo')


# if user_city[:5].find('SANTO') == 0:
#     print(f'A palavra está no começo')
# else:
#     print(f'Não começa com a palavra Santo')


pasqualiFinal.close()

