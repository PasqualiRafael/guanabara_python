from modulos import pasqualiFinal
from random import shuffle


pasqualiFinal.ini(f'Escolher a ordem da lista de alunos')


minha_lista = ['Rafael', 'Nanda', 'Gabi', 'Ana']
shuffle(minha_lista)
print('A ordem será: {}'.format(minha_lista))



pasqualiFinal.close()
