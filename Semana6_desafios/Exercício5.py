import random

saldo = 100
partidas_ganhas = 0
partidas_perdidas = 0

while saldo > 0:
    aposta_jogador = float(input(f'Saldo: R${saldo:.2f} . Qual o valor da sua aposta? '))
    if aposta_jogador <= saldo:
        dado = random.randint (1,6)
        dado1 = random.randint (1,6)
        soma = dado + dado1
        print(f'A soma dos dados {dado} e {dado1} é igual a {soma}')

        if soma == 7 or soma == 11:  
            saldo += aposta_jogador * 2  
            partidas_ganhas += 1  
            print(f"Você ganhou! Seu saldo agora é de R${saldo:.2f}.")
        else:
            saldo -= 20.00  
            partidas_perdidas += 1  
            print(f"Você perdeu! Seu saldo agora é de R${saldo:.2f}.")
    else: 
        print('Impossivel fazer essa aposta, saldo inválido')

        
    parada = input('Você quer continuar jogando? (S/N): ')
    if parada.lower() != 's':
        break

print(f"Pontos: R${saldo:.2f}")
print(f"Total de partidas que você ganhou: {partidas_ganhas}")
print(f"Total de partidas que você perdeu: {partidas_perdidas}")