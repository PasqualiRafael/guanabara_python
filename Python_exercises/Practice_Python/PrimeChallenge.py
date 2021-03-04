from my_modulos import pasqualiFinal

pasqualiFinal.ini("Prime Challenge")





def one():
    primo = int(input("Digite um numero:\n"))
    for x in range(2, primo + 1):
        if x != primo:
            if primo % x == 0:
                print("Ele não é primo")
                break
        else:
            print("Ele é primo")
    print("Fim")


one()


pasqualiFinal.close()
