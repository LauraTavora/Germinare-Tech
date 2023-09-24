lucas = 0
wellington = 0
gabriella = 0
voto_branco = 0
votos = 0 
opcoes_votos = 1,2,3,4

while (votos <= 20):
    votacao = int(input('Vote em um dos candidatos acima: '))


    print('[1] Lucas')
    if votacao == 1:
        lucas += 1 
    else:
        lucas += 0
    print('[2] Wellington')
    if votacao == 2:
        wellington += 1
    else:
        wellington += 0
    print('[3] Gabriella')
    if votacao == 3:
        gabriella += 1
    else:
        gabriella += 0
    print('[4] Voto em branco')
    if votacao == 4:
        voto_branco += 1
    else:
        voto_branco += 0
    
    


    votos += 1