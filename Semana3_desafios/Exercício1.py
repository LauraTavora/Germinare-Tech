texto = input('Escreva uma mensagem para invertê-la:')

def inverter_string(texto):
    return texto[::-1]

print(f'A mensagem invertida fica:{inverter_string(texto)}')