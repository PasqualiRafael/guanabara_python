from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini('Média dos Alunos')

user_cont = 'S'
geral = list()
copy = tuple()
alunos = list()
cont = 0
user_name = True


while user_cont == 'S':
    cont += 1
    name = str(input(f'Nome do aluno: ')).capitalize().strip()
    n1 = float(input(f'Primeira nota: '))
    n2 = float(input(f'Segunda nota: '))
    media = float((n1 + n2) / 2)
    geral.append(cont)
    geral.append(name)
    geral.append(n1)
    geral.append(n2)
    geral.append(media)
    copy = geral[:]
    alunos.append(copy)
    geral.clear()

    user_cont = str(input(f'Deseja continuar? S/N ')).upper().strip()
    if user_cont != 'S' and user_cont != 'N':
        print(f'Opção inválida. Tente de novo.')
        user_cont = str(input(f'Deseja continuar? S/N ')).upper().strip()


print('-=' * 4 + f'{cores["bw"]} Boletim dos alunos {cores["close"]}' + '=-' * 4)
print(f'No.  NOME        Média')
print('-=-' * 10)
for x in range(0, cont):
    print(f'{alunos[x][0]}  {alunos[x][1]}  {alunos[x][4]}')
print('-=-' * 10)


while True:
    user_name = str(input(f'Mostrar as notas de qual aluno? (999 interrompe)\n')).strip().capitalize()
    name = copy.index(user_name)
    print(name)

    if user_name == 999:
        break


'''
ficha = list()
while True:
    nome = str(input(f'Nome: '))
    n1 = float(input(f'Nota 1: '))
    n2 = float(input(f'Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input(f'Quer continuar? S/N'))
    if resp in 'Nn':
        break
print('--' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('--' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 30)
    opc = int(input(f'Mostrar a nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print(f'Finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte Sempre >>>')

'''
pasqualiFinal.close()