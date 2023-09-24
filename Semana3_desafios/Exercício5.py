import random
from math import factorial

def formatação(number):
    partes = "{:,.0f}".format(number).split(",")
    numero_formatado = ".".join(partes)
    return numero_formatado

def fatorial(A,B): 
    A = factorial(A)
    B = factorial(B)
    return A + B

A = random.randint(0,20)
B = random.randint(0,20)

fatorial_formatado = formatação(fatorial(A,B))

print(f'O valor de A é {A}')
print (f'O valor de B é {B}')
print(f'A soma do fatorial dos números A e B é {fatorial_formatado}')