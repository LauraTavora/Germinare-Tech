nome = str(input('Digite o nome de um lutador: '))
peso = float(input(f'Digite o peso do {nome}: '))

if peso < 65:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Pena!')
if peso >= 65 and peso < 72:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Leve!')
if peso >= 72 and peso < 79:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Ligeiro!')
if peso >= 79 and peso < 86:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Meio-médio!')
if peso >= 86 and peso < 93:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Médio!')
if peso >= 93 and peso < 100:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Meio-pesado!')
if peso >= 100:
    print(f'O lutador {nome} pesa {peso}Kg e se enquadra na categoria Pesado!')