# É uma das variaveis compostas, existem três tipos as tuplas(), os dicionarios{} e as listas[].
# são variaveis que guardam mais de uma informação por espaço


thistuple =('banana', 'apple', 'cherry')
print(thistuple[0])

for x in thistuple:
    print(x)
print('-=' * 30)

for y in range(0, len(thistuple)):
    print(f'Essas comidas {thistuple[y]}')

print('-=' * 30)
for pos, c in enumerate(thistuple):
    print(f'Essa {c} esta na posição {pos}°')

print('-=' * 30)
for y in range(0, len(thistuple)):
    print(f'Essas comidas {thistuple[y]} estão posição {y}°')

print('-=' * 30)
print(sorted(thistuple))

print('-=' * 30)
# Ele junta uma tupla em outra não soma os valores.
# metodo .count dentro da tupla mostra quantas vezes determinado numero apareceu.
# metodo .index, mostra em que posição está determinado numero.
a = (2, 3, 5)
b = (5, 9, 10, 3)
c = b + a
print(c)
print(c.count(5))
print(c.index(9))
