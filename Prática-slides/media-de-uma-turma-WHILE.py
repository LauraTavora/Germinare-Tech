alunos = int(input('Quantos alunos a turma tem? '))
contador = 1
média = 0 
while (contador <= alunos):
    nota1 = float(input('Digite a primeira nota'))
    nota2 = float(input('Digite a segunda nota'))
    nota3 = float(input('Digite a terceira nota'))
    media = (nota1+nota2+nota3)/3
    print('Média =',media)
    média = média + media
    if (media>=6):
        print('Aluno aprovado')
    else:
        print('aluno reprovado')
    contador +=1

media = média/alunos
print('a media da turma foi',media)