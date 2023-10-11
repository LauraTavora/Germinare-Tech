import random 

#################### DECIFRAR #################

# função decifrar sem chave

def decifrarSchave(mensagem):
#   for in range(0, 25):
    x = 0
    while x < 25:
        mensagemDecifrada = decifrarChave(mensagem,x)
        