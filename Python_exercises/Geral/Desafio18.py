from modulos import pasqualiFinal
from math import cos, sin, tan, radians

pasqualiFinal.ini(f'Cos, sen, tan')

user_grau = int(input(f'Qual o angulo?\n'))
user_rad = radians(user_grau)

print('O Angulo de {}, seu cosseno é: {:.2f}'.format(user_grau, cos(user_rad)))
print('O Angulo de {}, seu seno é: {:.2f}'.format(user_grau, sin(user_rad)))
if(user_grau == 90):
    print('A tangente de {}, é paralela ao angulo, portanto seu numero é infinito'. format(user_grau))
else:
    print('O Angulo de {}, sua tangente é: {:.2f}'.format(user_grau, tan(user_rad)))

pasqualiFinal.close()