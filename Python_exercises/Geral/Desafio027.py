from modulos import pasqualiFinal

pasqualiFinal.ini(f'Ler nome completo e mostrar o primeiro e o ultimo nome separadamente')

name = str(input('Digite o nome completo:\n')).title().strip()
# name: str = 'Ana Maria de Souza'.lower().strip()
list_name = name.split()

print(list_name)
print('O primeiro nome é: {}'.format(list_name[0]))
print('O ultimo nome é: {}'.format(list_name[-1]))

pasqualiFinal.close()

