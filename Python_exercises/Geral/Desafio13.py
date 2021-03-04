# Desafio13
print(f"Ler o salario, mais o aumento!\n")
print(f"")
# import

# input
user_aumento = int(input(f"Qual a porcentagem do aumento?\n"))

# var
funci_a = 998
funci_b = 2352.85
funci_c = 1000

x = 100

# cal
aument = (x + user_aumento) / 100
a = funci_a * aument
b = funci_b * aument
c = funci_c * aument

# function


def __cal__(v_in, v_fin):
    print(
        "O salario do funcionario e: R$: {:.2f} com o aumento de {}% ficara: R$: {:.2f}".format(
            v_in, user_aumento, v_fin
        )
    )


__cal__(funci_a, a)
__cal__(funci_b, b)
__cal__(funci_c, c)


def close():
    print(f"")
    input(f"Pressione qualquer tecla para fechar!")


close()
