from modulos import pasqualiFinal

pasqualiFinal.ini(f"Perfunte o salario, calcule o aumento, com diferença if")

# var
user_salary = float(input("Qual seu salário?\n"))
_b = 10
_a = 15

# calc
_baixo = (100 + _b) / 100
_alto = (100 + _a) / 100

# function

if user_salary <= 1250:
    print("Seu salário será: {} com aumento de {}%".format((user_salary * _alto), _a))
else:
    print("Seu salário será: {} com aumento de {}%".format((user_salary * _baixo), _b))


pasqualiFinal.close()
