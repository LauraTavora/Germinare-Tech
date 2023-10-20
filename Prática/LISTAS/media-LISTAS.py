boletim = []
alunos = int(input('Quantos alunos? '))
cont = 1
while cont <= alunos:
    nome = str(input(f'Digite o nome do aluno {cont}º: '))
    nota1 = float(input(f'Primeira nota de {nome}: '))
    nota2 = float(input(f'Segunda nota de {nome}: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome,[nota1,nota2],media])
    cont = cont + 1

print('N:  Alunos:  Média')
for i, a in enumerate(boletim):
    print(f'{i+1} {a[0]:^12} {a[2]}')