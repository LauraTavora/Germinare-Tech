# Random
import random

print(random.random()) # Valor de 0.0 até 1.0
print(random.uniform(4,10)) # Valor decimal do mínimo ao máximo
print(random.randint(12,55)) # Valor inteiro do mínimo ao máximo

cores = ['verde', 'vermelho','azul']
print(random.choice(cores)) # Escolher uma opção dentro de uma fonte

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4','carta5']
random.shuffle(cartas_de_um_baralho)
print(cartas_de_um_baralho)


# DESAFIOS!!!
'''
1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
2. Você quer fazer um sorteio entre 300 nomes em uma lista de nomes
3. Você quer escolher aleatóriamente um número de 10-100
4. Você quer escolher uma carta aleatóriamente dentro de um baralho
5. Você quer gerar nomes de usuário aleatóriamente
6. Você quer gerar senhas seguras
'''