from modulos import pasqualiFinal
from math import sin, cos, radians, tan


pasqualiFinal.ini(f'Encontrar o cos e sin do angulo')

# var
user_ang: int = 45
user_radians = radians(user_ang)

# cal
user_cos = cos(user_radians)
user_sin = sin(user_radians)
user_tan = tan(user_radians)

# Print
print('O angulo {}, seu cos: {:.2f} | sin: {:.2f}'.format(user_ang, user_cos, user_sin))

if user_ang == 90:
    print('A tangente de {}, é paralela ao angulo, portanto seu numero é infinito'.format(user_ang))
else:
    print('A tangente: {:.2f}'.format(user_tan))



pasqualiFinal.close()

