valor_emprestimo = float(input('Quanto você deseja pegar emprestado?'))
renda_atual = float(input('Qual a sua renda mensal atual?'))


while True:
    credito = input('Seu Score de crédito é acima de 450 pontos?:\n').strip().upper()
    if credito == 'SIM' or credito == 'NÃO':
        break
    else:
        print('Resposta inválida. Responda com "SIM" ou "NÃO" ')

while True:
    dividas = input('Você não possui dívidas ativas?:\n').strip().upper()
    if dividas == 'SIM' or dividas == 'NÃO':
        break
    else:
        print('Resposta inválida. Responda com "SIM" ou "NÃO" ')

while True:
    funcionario_publico = input('Você é funcionário público?:\n').strip().upper()
    if funcionario_publico == 'SIM' or funcionario_publico == 'NÃO':
        break
    else:
        print('Resposta inválida. Responda com "SIM" ou "NÃO" ')

while True:
    dados = input('Você concorda em compartilhar seus dados através do open banking:\n').strip().upper()
    if dados == 'SIM' or dados == 'NÃO':
        break
    else:
        print('Resposta inválida. Responda com "SIM" ou "NÃO" ')




respostas_positivas = 0 
if credito == 'SIM':
    respostas_positivas += 1
if dividas == 'SIM':
    respostas_positivas += 1 
if funcionario_publico == 'SIM':
    respostas_positivas += 1
if dados == 'SIM':
    respostas_positivas += 1 
if renda_atual >= (2 * valor_emprestimo):
    respostas_positivas += 1


if respostas_positivas >= 3:
    if respostas_positivas == 5:
        print(f'Sua pontuação foi de {respostas_positivas}')
        print(f'Aprovação Total, valor aprovado R${valor_emprestimo:.2f}')
    else: 
        print(f'Sua pontuação foi de {respostas_positivas}')
        valor_aprovado = 0.6 * valor_emprestimo
        print(f'Aprovado com desconto, valor aprovado R${valor_aprovado:.2f}')
elif respostas_positivas >= 2:
    print(f'Sua pontuação foi de {respostas_positivas}')
    valor_aprovado =  0.2 * valor_emprestimo
    print(f'Aprovado com restrições, valor aprovado R${valor_aprovado:.2f}')
else: 
    print ('Não aprovado')
