from modulos import pasqualiFinal

pasqualiFinal.ini(f'Quantas vezes a letra "a" aparece na frase')

user_frase = str.lower(input("Digite uma frase:\n")).strip()

print('A letra "a" aparece na frase {} vezes'.format(user_frase.count("a")))
print('A posição da primeira letra "a" na frase é {}'.format(user_frase.find("a") + 1))
print('A ultima posição da letra "a" na frase é {}'.format(user_frase.rfind("a") + 1))


pasqualiFinal.close()
