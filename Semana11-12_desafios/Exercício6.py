import random

quantidade_numeros = int(input('Informe a quantidade de números desejados: '))

gerando_numeros = []
positivos = 0
negativos = 0

for i in range(0, quantidade_numeros):
    numeros = random.randint(-100, 100)
    gerando_numeros.append(numeros)

for i in gerando_numeros:
    if i > 0:
        positivos += i
    else:
        negativos += i

print()
print('Números gerados automaticamente:')
print(gerando_numeros)
print()
print(f'Soma dos números positivos: {positivos}')
print(f'Soma dos números negativos: {negativos}')

