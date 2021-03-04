from modulos import pasqualiFinal

pasqualiFinal.ini(f'Conversor de dollar to real')

user_dollar = float(input(f'Quantos dolares voce tem?\n'))
_real = 3.27
_conv = _real * user_dollar

print('US${:.2f} é o mesmo que: R$: {:.2f}'.format(user_dollar, _conv))

pasqualiFinal.close()

