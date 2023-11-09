contador = 0
ordem = 1
for i in range(0, 3):
    quiz = float(input(f'Digite a nota do {ordem}º quiz: '))
    ordem += 1
    contador += quiz

media_quiz = contador / 3
#print(media_quiz)
print('-='*30)

contador1 = 0
ordem1 = 1
for k in range(0, 3):
    atividade_individual = float(input(f'Digite a nota da {ordem1} atividade prática: '))
    ordem1 += 1
    contador1 += atividade_individual

media_individual = contador1 / 3
#print(media_individual)
print('-='*30)

contador2 = 0
ordem2 = 1
for j in range(0, 2):
    atividade_grupo = float(input(f'Digite a nota da {ordem2}º atividade em grupo: '))
    ordem2 += 1
    contador2 += atividade_grupo

media_grupo = contador2 / 2
#print(media_grupo)
print('-='*30)

hackathon = float(input('Digite a sua nota do hackathon: '))
avaliacao_final = float(input('Digite a sua nota da avaliação final: '))

N1 = (media_quiz * 0.2) + (media_individual * 0.3) + (media_grupo * 0.2) + (hackathon * 0.3)
N2 = avaliacao_final
NF = (N1 * 0.6) + (N2 * 0.4)

print(f'A sua média final no curso preparatório da Germinare Tech é igual a {NF:.2f}')