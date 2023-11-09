import random
from time import sleep

lista_A = []
lista_B = []

A = int(input('Informe o tamanho da lista A: '))

for i in range(0, A):
    lista_A.append(random.randint(1, 100))
print(f'listaA = {lista_A}')

print()

B = int(input('Informe o tamanho da lista B: '))

for i in range (0, B):
    lista_B.append(random.randint(1, 100))
print(f'listaB = {lista_B}')


lista_resultante = lista_A + lista_B
print()
sleep(1)
print(f'Lista resultante: {lista_resultante}')