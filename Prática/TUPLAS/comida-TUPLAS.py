lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')


# Vai printar apenas as comidas
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('='*40)

# Jeito 1 de printar comida e posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('='*40)

# Jeito 2 de printar comida de posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')



################################################################
# sorted

print(sorted(lanche)) # Vai printrar o lanche em ordem, isso não altera a Tupla original
print(lanche) # Mostra a tupla da maneira como foi escrita