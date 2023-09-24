from random import randint 

numero = randint(1,20)
tentativas = 0 
while True:
    chute = int(input('Digite um número aleatório: '))
    tentativas += 1 
    if chute > numero:
        print('Você digitou um número maior')
    elif chute < numero:
        print('Você digotu um número menor')
    else:
        print(f'Você acertou o número em {tentativas} tentativas. Parabéns')
        break

print('Fim do jogo')