aluno = {}
aluno['Nome'] = input('Nome:\n')
print('A média de', aluno['Nome'], 'foi de:')
aluno['Média'] = float(input())
if (aluno['Média'] >= 6):
    aluno['Situação']='Aprovado'
elif (aluno['Média'] >= 4 and aluno['Média'] < 6):
    aluno['Situação']='Recuperação'
else:
    aluno['Situação']='Reprovado'
print('=*' * 25)
for i in aluno:
    print(i,':',aluno[i])