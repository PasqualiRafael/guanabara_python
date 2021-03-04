from modulos import pasqualiFinal

pasqualiFinal.ini(f'Ler um numero e mostrar a unidade separada')

user_num = int(input('Escolha um numero qualquer:\n'))
#user_num = int(585)
user_num = str(user_num)

user_lis = user_num.split()
user_c = len(user_lis[0])

print(user_c)
print(user_lis)

if(user_c == 1):
    print(user_lis[0][0])
elif(user_c == 2):
    print(user_lis[0][0])
    print(user_lis[0][1])
elif(user_c == 3):
    print(user_lis[0][0])
    print(user_lis[0][1])
    print(user_lis[0][2])
elif(user_c == 4):
    print(user_lis[0][0])
    print(user_lis[0][1])
    print(user_lis[0][2])
    print(user_lis[0][3])
else:
    print(f'Voce precisa selecionar um valor entre 0 e 9999.')

pasqualiFinal.close()