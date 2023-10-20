from random import randint

n = int(input('Quantos jogos deseja fazer? '))
megasena = []
for i in range(n):
    jogo = []
    for i in range(6):
        jogo.append(randint(1,60))
        jogo.sort()
    megasena.append(jogo)
cont = 1
for i in megasena:
    print('Jogo',cont,'=',i)
    cont += 1