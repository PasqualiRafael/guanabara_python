from random import randint
from modulos import pasqualiFinal
from modulos.colors import cores

pasqualiFinal.ini("Par ou impar jogo")

pc = n = cont = 0
opc = ""

while True:
    print("[P] Par\n" + "[I] Impar\n")
    opc = str(input("Digite a letra: ")).upper().strip()[0]
    n = int(input("Jogue um numero: "))
    print("")
    pc = randint(1, 2)
    if n < 0:
        print("Escolha um numero que não seja negativo")
    else:
        if opc in "P":
            if (n + pc) % 2 == 0:
                cont += 1
                print(
                    f'{cores["green"]}Voce venceu!{cores["close"]}'
                    + f'\nVoce jogou: {cores["yellow"]}{n}{cores["close"]}'
                    + f'\nPc jogou: {cores["yellow"]}{pc}{cores["close"]}'
                )
                print("~" * 20)
            else:
                break
        elif opc in "I":
            if (n + pc) % 2 == 1:
                cont += 1
                print(
                    f'{cores["green"]}Voce venceu!{cores["close"]}'
                    + f'\nVoce jogou: {cores["yellow"]}{n}{cores["close"]}'
                    + f'\nPc jogou: {cores["yellow"]}{pc}{cores["close"]}'
                )
                print("~" * 20)
            else:
                break
        else:
            print("~" * 20)
            print("Escolha par ou impar")
            print("")

print(f'{cores["red"]}Voce perdeu!{cores["close"]}\nVoce jogou: {n}\nPc jogou: {pc}')
print(f'Voce ganhou {cores["yellow"]}{cont}{cores["close"]} seguidas.')
