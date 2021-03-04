from modulos import pasqualiFinal

pasqualiFinal.ini(f'Numeros por extenso')

# var
extenso = (
    "zero",
    "um",
    "dois",
    "tres",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)

# laço
while True:
    num = int(input(f'Digite um numero entre 0 e 20.\n'))
    if 0 <= num <= 20:
        print(f'Voce escolheu o numero: {extenso[num]}')
        break
    else:
        print('Voce precisa digitar um numero entre 0 e 20!')

print('Fim')

pasqualiFinal.close()
