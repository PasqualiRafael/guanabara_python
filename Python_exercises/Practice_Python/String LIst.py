from modulos import pasqualiFinal

pasqualiFinal.ini('String Lists')

user_string = str(input('Diga uma frase: ')).lower()
user_string_list = user_string.strip().split()
user_string_join = ''.join(user_string_list)

if user_string == user_string_join[::-1]:
    print('Essa frase é um palindrome')
    print('{}\n{}'.format(user_string, user_string_join))
else:
    print('Essa frase não é um palindrome')
    print('{}\n{}'.format(user_string, user_string_join))



pasqualiFinal.close()
