import random 

#################### DECIFRAR #################

# função decifrar sem chave

def decifrarSchave(mensagem):
#   for in range(0, 25):
    x = 0
    while x < 25:
        mensagemDecifrada = decifrarChave(mensagem,x)
        print('**********************************************************')
        print(' ')
        print(f'Mensagem Cifrada: \n(mensagem)\n\nMensagem Cifrada:\n{mensagemDecifrada}\n\nChave Utilizada:\n{x}')
        print(' ')
        print('**********************************************************')
        resposta = input('A mensagem foi decifrada? (s/n) ').lower()
        if(resposta == 's'):
            print('O Sistema está sendo finalizado')
            break
        x = x + 1


# função para decifrar a mensagem
def decifrarChave(mensagem,chave):
    mensagemDecifrada = ''
    # for x in mensagem:
    x = 0
    while x < len(mensagem):
        mensagemDecifrada += decifrarLetra(mensagem[x],chave)
        x = x + 1
    return mensagemDecifrada

# função para decifrar uma letra com a cifra de cesar
def decifrarLetra(Letra,chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letraDecifrada = ''

    if(Letra == ' '):
        return Letra
    
    # encontrando a posicao de letra no alfabeto
    # for x in range(0,len(alfabeto)):
    x = 0
    while x < len(alfabeto):
        if Letra == alfabeto[x]:
            posicao = x
        x = x + 1

  # movimentando a letra de acordo com a chave
    posicao = posicao - chave
    if(posicao < 0):
        posicao = posicao + (len(alfabeto))
    letraDecifrada = alfabeto[posicao]

    return letraDecifrada

#################################################################


############################ CIFRAR #############################

def cifrarSChave(mensagem):
    chaveAleatoria = random.randint(0,25)
    mensagemCifrada = cifrarChave(mensagem,chaveAleatoria)
    print('**************************************************************')
    print(' ')
    print(f'Mensagem:\n{mensagem}\n\nMensagem Cifrada:\n{mensagemCifrada}\n\nChave utilizada:\n{chaveAleatoria}')
    print(' ')
    print('***************************************************************')



# função para cifrar utilizando uma chave inteira positiva
def cifrarChave(mensagem, chave):
    mensagemCifrada = ' '
    x = 0
    # for x in mensagem:
    while x < len(mensagem):
        mensagemCifrada += cifrarLetra(mensagem[x],chave)
        x = x + 1
    return mensagemCifrada


    
# função para cifrar uma letra com a cifra de cesar
def cifrarLetra(mensagem,chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mensagemCifrada = ' '

    if(mensagem == ' '):
        return mensagem
    
   # encontrando a posição da mensagem no alfabeto
    # for x in range(0,len(alfabeto)):
    x = 0
    while x < len(alfabeto):
        if mensagem == alfabeto[x]:
            posicao = x
        x = x + 1
        

   # movimentando a mensagem de acordo com a chave
    posicao = posicao + chave
    if(posicao > len(alfabeto)-1):
        posicao = posicao - (len(alfabeto))
    mensagemCifrada = alfabeto[posicao]

    return mensagemCifrada

###########################################################


######################## INTERFACE ########################

def interfaceCifra():
  while True:
    print("""
         1. Cifrar Mensagem (com chave)
         2. Decifrar Mensagem (com chave)
         3. Cifrar Mensagem (sem chave)
         4. Decifrar Mensagem (sem chave)
         5. SAIR           
      """)
    escolha = int(input('Escolha uma das opções acima: '))
    if (escolha > 5 or escolha < 1):
        print('ERRO! OPÇÃO INVÁLIDA')
    else:
      while True:
        if escolha == 1 or escolha == 2:
          mensagem = input('Informe a mensagem de interese:\n').lower()
          chave = int(input('Informe a chave a ser utilizada:\n'))
          if chave < 0:
              print('ERRO!! CHAVE INVÁLIDA! INFORME UM NÚMERO POSITIVO')
          else:
            if escolha == 1:
                mensagemCifrada = cifrarChave(mensagem,chave)
                print('*******************************************************************')
                print(' ')
                print(f'Mensagem:\n{mensagem}\n\nMensagem Cifrada:\n{mensagemCifrada}')
                print(' ')
                print('*******************************************************************')
                verificarContinuidade()
            else:
                mensagemDecifrada = decifrarChave(mensagem,chave)
                print('*******************************************************************')
                print(' ')
                print(f'Mensagem Cifrada:\n{mensagem}\n\nMensagem Cifrada:\n{mensagemDecifrada}')
                print(' ')
                print('********************************************************************')
                verificarContinuidade()
            break
        elif escolha == 3:
             mensagem = input('Informe a mensagem de interesse:\n').lower()
             cifrarSChave(mensagem)
             verificarContinuidade()
             break
        else:
            print('O sistema está sendo finalizado')
            break
    break
  
# função para verificar a continuidade
def verificarContinuidade():
    continuidade = input('Deseja continuar? (s/n) ').lower()
    if continuidade == 's':
        interfaceCifra()

########################################################

interfaceCifra()