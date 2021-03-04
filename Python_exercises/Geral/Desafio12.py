#Desafio12
print(f'Preco e desconto!\n')
print(f'')
#input
sabao = 7.90
coka_cola = 4.80
bife = 22.89

user_desconto = int(input('Qual a porcentagem de desconto?\n'))
x  = 100
desconto = (x - user_desconto) / 100
valor_sabao = sabao * desconto
valor_coka = coka_cola * desconto
valor_bife = bife * desconto

print('O sabao custa: {:.2f} com o {}% de desconto, ficará: {:.2f}'.format(sabao, user_desconto, valor_sabao))
print('O coka custa: {:.2f} com o {}% de desconto, ficará: {:.2f}'.format(coka_cola, user_desconto, valor_coka))
print('O bife custa: {:.2f} com o {}% de desconto, ficará: {:.2f}'.format(bife, user_desconto, valor_bife))



def close():
    print(f'')
    input(f'Pressione qualquer tecla para fechar!')

close()