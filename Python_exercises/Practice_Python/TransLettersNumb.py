#Transforme
print(f'Transformar letras em numeros!\n')
print(f'')
#import


#var
intab = 'aeiostb'
outtab = '4310578'
trans = str.maketrans(intab, outtab)
msg = (f'''Este pequeno texto serve apenas para mostrar como nossa cabeça consegue fazer coisas impressionantes! Repare\n
nisso! No começo estava mais complicado, mas nessa linha sua cabeça esta decifrando o codigo quase que automaticamente,\n
sem precisar pensar muito, certo? Intrigante.''')

#input
x = input(f'Escreva uma frase, sem usar acento.\n')

print(x.translate(trans))
print(f'')
print(f'Vou escrever outro texto abaixo tente ler\n')
print(f'')
print(msg.translate(trans))
print(f'')

def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()