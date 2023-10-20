alunos = int(input('Quantos alunos tem na turma? '))
geral = 0
media_abaixo = 0
media = []

for quantidade_alunos in range(1, alunos + 1):
    nome = str(input(f'Nome do {quantidade_alunos}º aluno: '))
    nota1 = int(input(f'Digite a primeira nota de {nome}: '))
    nota2 = int(input(f'Digite a segunda nota de {nome}: '))
    conta_media = (nota1 + nota2) / 2

    if conta_media >= 7:
        conceito = 'Aprovado'
    else:
        conceito = 'Reprovado'
        media_abaixo += 1
        
    geral += conta_media
    media.append((quantidade_alunos, nome, nota1, nota2, conta_media, conceito))

print()
print('N:   Alunos:   Nota1:   Nota2:   Média:   Conceito:')
for i in media:
    quantidade_alunos, nome, nota1, nota2, media, conceito = i
    print(f'{quantidade_alunos:^2}   {nome} \t{nota1:.1f}\t{nota2:.1f}\t {media:.1f}\t  {conceito:^1}') 

print()
media_turma = geral / alunos
print(f'A média da turma foi: {media_turma:.0f}')

if media_abaixo <= 1:
    print(f'A turma teve {media_abaixo} aluno abaixo da média')
else:
    print(f'A turma teve {media_abaixo} alunos abaixo da média')