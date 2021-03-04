from modulos import pasqualiFinal

pasqualiFinal.ini(f'Digite um nome e verifique se tem a palavra SILVA')

# input
user_name = str.upper(input('Digite um nome de uma cidade: '))

# function

if 'SILVA' in user_name:
    print(f'Tem silva no nome digitado')
else:
    print(f'Não tem silva no nome digitado')


pasqualiFinal.close()

