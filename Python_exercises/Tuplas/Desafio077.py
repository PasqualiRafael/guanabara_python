from modulos import pasqualiFinal

pasqualiFinal.ini(f'Contando vogais')

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for x in palavras:
    print(f'\nNa palavra {x.upper()}, temos: ', end='')
    for c in x:
        if c.lower() in 'aeiou':
            print(c, end=' ')

pasqualiFinal.close()
