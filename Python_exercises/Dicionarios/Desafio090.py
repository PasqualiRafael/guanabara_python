nome = str('Rafael')
media = float(6.5)
aluno = {'Nome': nome, 'Media': media}

if media <= 5:
    print(f"O {aluno['Nome']} foi reprovado, com a média {aluno['Media']}")
else:
    print(f"{aluno['Nome']} foi aprovado, com a média {aluno['Media']}")

