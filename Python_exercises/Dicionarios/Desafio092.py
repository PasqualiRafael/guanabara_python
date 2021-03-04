

geral = {}
geral['Nome'] = str(input(f'Qual o nome: '))
geral['Ano'] = int(input(f'Ano de nascimento: '))
geral['ctps'] = int(input(f'Possui carteira de trabalho? (0 caso não possui) '))
if geral['ctps'] != 0:
    geral['Contra'] = int(input(f'Qual o ano de contratação: '))
    geral['salario'] = int(input(f'Qual o salario: '))
    apos = int(geral['Contra'] + 35)
    vida = int(apos - geral['Ano'])
    print(f"O {geral['Nome']} irá se aposentar com {vida} anos")
    print(geral)
else:
    print(geral)

