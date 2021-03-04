from modulos import pasqualiFinal

pasqualiFinal.ini(f'Calculo de tinta')

_h: float = 3
_c: float = 4
_a: float = _h * _c

_tinta: int = 2
_lata: float = _a / _tinta

print('Voce irá precisar de {:.2f} de latas de tinta, para pintar {:.2f} de area.'.format(_lata, _a))

pasqualiFinal.close()

