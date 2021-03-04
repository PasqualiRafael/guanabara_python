from modulos import pasqualiFinal

pasqualiFinal.ini('Desconto')

_cost: float = 100
_desc: float = 5
_caldesc: float = (100 - _desc) / 100
_fcost = _cost * _caldesc

print(_fcost)

pasqualiFinal.close()

