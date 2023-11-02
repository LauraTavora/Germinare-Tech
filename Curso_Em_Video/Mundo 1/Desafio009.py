# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver a sua tabuada: '))
print('-=' *20)
print(f'{num} x {1} = {num * 1}')
print(f'{num} x {2} = {num * 2}')
print(f'{num} x {3} = {num * 3}')
print(f'{num} x {4} = {num * 4}')
print(f'{num} x {5} = {num * 5}')
print(f'{num} x {6} = {num * 6}')
print(f'{num} x {7} = {num * 7}')
print(f'{num} x {8} = {num * 8}')
print(f'{num} x {9} = {num * 9}')
print(f'{num} x {10} = {num * 10}')
print('-=' *20)

# OU
print()

print('-=' *20)
for contador in range(1, 11):
    print(f'{num} x {contador} = {num * contador}')
print('-=' *20)