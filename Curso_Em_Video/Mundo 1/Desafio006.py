# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


import math

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print(f'O dobro de {num} vale {dobro}.')
print(f'O triplo de {num} vale {triplo}.')
print(f'A raiz quadrada de {num} é igual a {raiz:.2f}.')