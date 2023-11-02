# Faça um program que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1

print(f'Analisando o valor {num}, seu antecessor é {antecessor} e o sucessor é {sucessor}')

# OU

print(f'Analisando o valor {num}, seu antecessor é {num - 1} e o sucessor é {num + 1}')