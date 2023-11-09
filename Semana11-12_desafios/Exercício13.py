import random

def gerando_numeros():
    numeros = []
    for i in range(1000):
        numero = random.randint(0, 10)
        numeros.append(numero)
    return numeros

def mais_sorteado(numeros):
    contagem = {}
    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    mais_vezes = max(contagem, key=contagem.get)
    return mais_vezes

def menos_sorteado(numeros):
    contagem = {}
    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    menos_vezes = min(contagem, key=contagem.get)
    return menos_vezes

def maior_numero(numeros):
    numero_maior = max(numeros)
    return numero_maior

def menor_numero(numeros):
    numero_menor = min(numeros)
    return numero_menor

numeros_aleatorios = gerando_numeros()

aparece_mais = mais_sorteado(numeros_aleatorios)
aparece_menos = menos_sorteado(numeros_aleatorios)

maior = maior_numero(numeros_aleatorios)
menor = menor_numero(numeros_aleatorios)

print(f'O número sorteado mais vezes foi: {aparece_mais}')
print(f'O número sorteado menos vezes foi: {aparece_menos}')
print(f'O maior número sorteado foi: {maior}')
print(f'O menor número sorteado foi: {menor}')
