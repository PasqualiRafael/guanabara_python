from modulos import pasqualiFinal

pasqualiFinal.ini(f"campeonato brasileiro")

# var
turple: str = (
    "Os gansos",
    "Caneludos FC",
    "Unidos da perna da pau",
    "Boleiros",
    "Canarinhos",
    "Rasga tudo futebol clube",
    "Os várzeas",
    "Só nerds",
    "Oscar Alhos",
    "Girinos FC",
    "Esquimoses",
    "Do mangue",
    "Sanguessugas",
    "Cachorro doido",
    "Viadanis",
    "Perobus FC",
    "Só noize",
    "Bêbados da várzea",
    "Jumentus futebol clube",
)
print("-=" * 30)
print(f"Os cinco primeiros são: {turple[:5]}")
print("-=" * 30)
print(f"Os quatro ultimos são: {turple[-1: -5: -1]}")
# print(f'Os quatro ultimos são: {turple[-4:]}') Mesma coisa do que o comando acima
print("-=" * 30)
print(f"Os times em ordem alfabética: {sorted(turple)}")
print("-=" * 30)
print(f"O time Do mangue está na posição: {turple.index('Do mangue') + 1}")
print("-=" * 30)
