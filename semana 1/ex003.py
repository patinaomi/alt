notas_aluno = []

for i in range(4):
    nota = float(input(f'Digite a {i+1}ª nota do aluno: '))
    notas_aluno.append(nota)

media = sum(notas_aluno) / len(notas_aluno)

if media >= 7:
    print(f'O aluno está APROVADO com média {media}')
elif media >= 4.9:
    print(f'O aluno está em RECUPERAÇÃO com média {media}')
else:
    print(f'O aluno está REPROVADO com média {media}')
