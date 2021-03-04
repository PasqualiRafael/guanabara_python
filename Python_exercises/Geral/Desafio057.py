from modulos import pasqualiFinal

pasqualiFinal.ini('Ler sexo')
'''
if user_sex != 'M' and user_sex != 'F':
    print('Voce precisa digitar ou M ou F')
'''

user_sex = ''
while user_sex != 'M' and user_sex != 'F':
    user_sex = str(input('Qual o sexo: [M/F]')).upper()[0].strip()
    if user_sex not in 'MF':
        print('Voce precisa digitar ou M ou F')

if user_sex == 'M':
    print('Você é homem')
else:
    print('Voce é mulher')




pasqualiFinal.close()
