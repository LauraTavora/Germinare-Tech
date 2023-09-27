lucas = 0
wellington = 0
gabriella = 0
votos_validos = 0 

while True:

    print('[1] Lucas')
    print('[2] Wellington')
    print('[3] Gabriella')
    print('[4] Voto em branco')

    votacao = int(input('Vote em um dos candidatos acima: '))

    if votacao == 1:
        votos_validos += 1
        lucas += 1
    elif votacao == 2:
        votos_validos += 1
        wellington += 1
    elif votacao == 3:
        votos_validos += 1
        gabriella += 1
    else:
        votos_validos += 0
        lucas += 0
        wellington += 0 
        gabriella += 0

    parada = input('Você quer continuar inserindo votos? ')
    if parada.lower() != 's':
        break

candidato_1 = 'Lucas'
candidato_2 = 'Wellington'
candidato_3 = 'Gabriella'

if lucas > wellington and lucas > gabriella:
    vencedor = candidato_1
    resultado = (lucas / votos_validos) * 100
elif wellington > lucas and wellington > gabriella:
    vencedor = candidato_2
    resultado = (wellington / votos_validos) * 100
else:
    vencedor = candidato_3
    resultado = (gabriella / votos_validos) * 100
        
           
print('==========RESULTADO=========')

print(f'Votos válidos: {votos_validos}')
print(f'O vencedor foi {vencedor} com {resultado:.2f}%')
print('='*28)
