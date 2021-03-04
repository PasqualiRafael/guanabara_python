from modulos import pasqualiFinal

pasqualiFinal.ini('Leia os lados e diz se é possivel formar um triangulo')

# var
lado_a = float(input('Qual o comprimento da primeira reta?\n'))
lado_b = float(input('Qual o comprimento da primeira reta?\n'))
lado_c = float(input('Qual o comprimento da primeira reta?\n'))

'''
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < b + a:
    print('Eles formam um triangulo.')
else:
    print('Eles não formam um triangulo.')

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('formam')
else:
    print('Não')
'''

# calc
modu_a = (lado_a - lado_c)
modu_b = (lado_a - lado_c)
modu_c = (lado_a - lado_b)

soma_a = (lado_b + lado_c)
soma_b = (lado_a + lado_c)
soma_c = (lado_a + lado_b)

# func
if (modu_a < lado_a) and (lado_a < soma_a):
    if (modu_b < lado_b) and (lado_b < soma_b):
        if (modu_c < lado_c) and (lado_c < soma_c):
            print('As restas {}, {}, {} conseguem formar um triangulo'.format(lado_a, lado_b, lado_c))
        else:
            print('Essas retas não formam um triangulo')
    else:
        print('Essas retas não formam um triangulo')
else:
    print('Essas retas não formam um triangulo')


pasqualiFinal.close()
