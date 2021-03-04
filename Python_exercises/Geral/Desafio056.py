from modulos import pasqualiFinal

pasqualiFinal.ini('Input nome idade e sexo e compare')

# var
s_idade = 0
nameold = ''
idadeold = 0
womanold20 = 0

# laço
for c in range(1, 5):
    print('------ {} -----'.format(c))
    name = str(input('Qual o nome: ')).strip()
    idade = int(input('Qual a idade: '))
    sexo = str(input('[M/F]: ')).strip()
    s_idade += idade
    if sexo in 'Ff' and idade < 20:
        womanold20 += 1
    if c == 1 and sexo in 'Mm':
        idadeold = idade
        nameold = name
    if sexo in 'Mm' and idade > idadeold:
        idadeold = idade
        nameold = name

print('')
print('A média de idade do grupo é: {}'.format(s_idade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadeold, nameold))
print('Ao todo são {} mulheres menores de 20 anos'.format(womanold20))

pasqualiFinal.close()
