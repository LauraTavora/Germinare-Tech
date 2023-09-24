import random

A1 = random.randint(1, 20)
B1 = random.randint(1, 20)
resultado_primeira = A1 * B1 
primeira_questao = int(input(f'Qual é o resultado de {A1} x {B1}? '))

A2 = random.randint(1, 20)
B2 = random.randint(1, 20)
resultado_segunda = A2 * B2 
segunda_questao = int(input(f'Qual é o resultado de {A2} x {B2}? '))

A3 = random.randint(1, 20)
B3 = random.randint(1, 20)
resultado_terceira = A3 * B3
terceira_questao = int(input(f'Qual é o resultado de {A3} x {B3}? '))

A4 = random.randint(1, 20)
B4 = random.randint(1, 20)
resultado_quarta = A4 * B4
quarta_questao = int(input(f'Qual é o resultado de {A4} x {B4}? '))

A5 = random.randint(1, 20)
B5 = random.randint(1, 20)
resultado_quinta = A5 * B5
quinta_questao = int(input(f'Qual é o resultado de {A5} x {B5}? '))

def acertos_atuais(primeira_questao,segunda_questao,terceira_questao,quarta_questao,quinta_questao):

    acerto1 = 0
    acerto2 = 0 
    acerto3 = 0 
    acerto4 = 0 
    acerto5 = 0 

    if primeira_questao == resultado_primeira:
        acerto1 += 1
    else:
        acerto1 += 0 
    if segunda_questao == resultado_segunda:
        acerto2 = acerto1 + 1
    else: 
        acerto2 = acerto1 + 0
    if terceira_questao == resultado_terceira:
        acerto3 = acerto2 + 1
    else:
        acerto3 = acerto2 + 0 
    if quarta_questao == resultado_quarta:
        acerto4 = acerto3 + 1
    else: 
        acerto4 = acerto3 + 0
    if quinta_questao == resultado_quinta:
        acerto5 = acerto4 + 1
    else: 
        acerto5 = acerto4 + 0 


    print(f'Pergunta: {A1} x {B1} = {resultado_primeira}')
    if primeira_questao == resultado_primeira:
        print('Acertou')
        print(f'Acertos atuais: {acerto1}')
        print('')
    else: 
        print('Errou')
        print(f'A resposta correta era {resultado_primeira:.0f}')
        print(f'Acertos atuais: {acerto1}')
        print('')
    print(f'Pergunta: {A2} x {B2} = {resultado_segunda}')
    if segunda_questao == resultado_segunda:
        print('Acertou')
        print(f'Acertos atuais: {acerto2}')
        print('')
    else: 
        print('Errou')
        print(f'A resposta correta era {resultado_segunda:.0f}')
        print(f'Acertos atuais: {acerto2}')
        print('')

    print(f'Pergunta: {A3} x {B3} = {resultado_terceira}')    
    if terceira_questao == resultado_terceira:
        print('Acertou')
        print(f'Acertos atuais: {acerto3}')
        print('')
    else: 
        print('Errou')
        print(f'A resposta correta era {resultado_terceira:.0f}')
        print(f'Acertos atuais: {acerto3}')
        print('')
    print(f'Pergunta: {A4} x {B4} = {resultado_quarta}')
    if quarta_questao == resultado_quarta:
        print('Acertou')
        print(f'Acertos atuais: {acerto4}')
        print('')
    else: 
        print('Errou')
        print(f'A resposta correta era {resultado_quarta:.0f}')
        print(f'Acertos atuais: {acerto4}')
        print('')
    print(f'Pergunta: {A5} x {B5} = {resultado_quinta}')
    if quinta_questao == resultado_quinta:
        print('Acertou')
        print(f'Acertos atuais: {acerto5}')
    else: 
        print('Errou')
        print(f'A resposta correta era {resultado_quinta:.0f}')
        print(f'Acertos atuais: {acerto5}')

acertos_atuais(primeira_questao,segunda_questao,terceira_questao,quarta_questao,quinta_questao)