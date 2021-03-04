from my_modulos.colors import cores


frase = 'Estou testando a funcionalidade'

def analisy():
    # Analisy
    print('-' * 12)
    print(f'{cores["bw"]}Analisy {cores["close"]}')

    # Contar a quantidade de letras na frase
    print(len(frase))

    # Contar a quantidade de letras 'parametro' que aparece no texto
    print(frase.count('a'))

    # Contar a quantidade de letras 'parametro' que aparece no texto, de tal char, até -1 char
    print(frase.count('a', 0, 13))

    # Encontrar a string no texto
    print(frase.find('fun'))

    # Encontrar a string no texto, se não houver ele retornará -1
    print(frase.find('android'))

    # Verificar se existe dentro, valor booleano
    print('testando' in frase)


def transformation():
    # Transformação
    print('-' * 12)
    print('Transformation')

    # Trocar uma palavra por outra
    print(frase.replace('testando', 'brincando'))

    # Colocar maiusculo só a primeira letra
    print(frase.capitalize())

    # Colocar maiusculo todos as primeiras letras
    print(frase.title())

    # Ele irá remover os espaços de ambos lados dados atoa na string, e irá fazer a contagem de char corretamente.
    # Divisão Lista se usa tambem o split, ele irá transformar uma frase em uma list.
    frase01 = '   espaço a toa dado no começo e fim   '
    juntar = frase01.strip().split()
    print(frase01.strip().split(' '))

    # Mesmo comando só que apagando só do lado direito e esquedo
    print(frase01.rstrip())
    print(frase01.lstrip())

    # Junção juntar a frase de novo escolhendo seu 'parametro' de junção
    print(f'{cores["red"]}Juntando {cores["close"]}')
    print(' '.join(juntar))

    # Deletar
    del frase01


def fatiamento():
    # Fatiamento de string
    print('-' * 12)
    print('Fatiamento de string')

    # Pegar o nono char
    print(frase[9])
    # Colocar o nono em maisculo
    print(frase[9].upper())
    # Selecionar do sexto ao 14 - 1 para mostrar
    print(frase[6:14].upper())
    # Agora pulando 1 char
    print(frase[6:14:2].upper())
    # Ele vai começar sempre do 0, até -1 do 6
    print(frase[:6])
    # Ele vai começar sempre do 6, até final
    print(frase[6:])
    # Ele vai começar sempre do 6, até final, mas pulando 2 char
    print(frase[6::3])
    # Centralizar texto
    print('{:^40}'.format('Texto centralizado'))
    print('{:-^40}'.format(' Texto centralizado '))


def func(user_num):
    if user_num == 'analisy':
        analisy()
    elif user_num == 'transformation':
        transformation()
    elif user_num == 'fatiamento':
        fatiamento()
    else:
        print(f'Escolha apenas uma das opções')


print(f'Na frase: ')
print(f'{cores["red"]}{frase}{cores["close"]}')
print('\n')

user_str = str(input(f'{cores["bw"]}Escreva a opção desejada:{cores["close"]} \nanalisy\ntransformation\nfatiamento\n\n'))
user_str = user_str.lower()
func(user_str)

