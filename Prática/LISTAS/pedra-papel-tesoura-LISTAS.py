from random import randint
computador = randint(0,2)
escolha = ('Pedra','Papel','Tesoura')
while True:
    print('Opções:')
    print('[1]-Pedra')
    print('[2]-Papel')
    print('[3]-Tesoura')

    while True:
        jogador = int(input('Qual sua jogada? '))
        jogador = jogador - 1
        if (jogador < 3):
            break
        else:
            print('Opção Inválida!')
    print('O computador escolheu', escolha[computador].upper())
    print('Você escolheu', escolha[jogador].upper())
    if computador == 0: #computador == pedra
        if jogador == 0:
            print('Deu EMPATE')
        elif jogador == 1:
            print('PARABÉNS! Você venceu')
        elif jogador == 2:
            print('IHH! Você perdeu')
    elif computador == 1: #computador == papel
        if jogador == 0:
            print('IHH! Você perdeu')
        elif jogador == 1:
            print('Deu EMPATE')
        elif jogador == 2:
            print('PARABÉNS! Você venceu')
    elif computador == 2: #computador == tesoura
        if jogador == 0:
            print('PARABÉNS! Você venceu')
        elif jogador == 1:
            print('IHH! Você perdeu')
        elif jogador == 2:
            print('Deu EMPATE')
    continuar = str(input('Deseja continuar? [s/n]: '))
    if continuar in ('n','não','nao'):
        print('Até a próxima')
        break
    else:
        print('=' * 30)