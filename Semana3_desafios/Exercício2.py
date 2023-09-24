texto = input('Escreva uma mensagem para invertê-la:')


def inverter_string(texto):
    return texto[::-1]


print(f'A mensagem invertida fica: {inverter_string(texto)}')


def contar_vogais(texto):
    
    return texto.count('a') + texto.count('e') + texto.count('i') + texto.count('o') + texto.count('u') + texto.count('â') + texto.count('ê') + texto.count('î') + texto.count('ô') + texto.count('û') + texto.count('á') + texto.count('é') + texto.count('í') + texto.count('ó') + texto.count('ú') + texto.count('ã') + texto.count('õ') + texto.count('à') + texto.count('A') + texto.count('E') + texto.count('I') + texto.count('O') + texto.count('U') + texto.count('Á') + texto.count('É') + texto.count('Í') + texto.count('Ó') + texto.count('Ú') + texto.count('Â') + texto.count('Ê') + texto.count('Î') + texto.count('Ô') + texto.count('Û') + texto.count('Ã') + texto.count('Õ') + texto.count('À')


print(f'O número de vogais que existe na mensagem é: {contar_vogais(texto)}')