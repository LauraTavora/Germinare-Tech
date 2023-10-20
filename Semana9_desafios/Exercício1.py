import math

vendedores = int(input('São quantos vendedores? '))

salarios = []
for quantidade_vendedores in range(1, vendedores + 1):
    salario = int(input(f'Qual é a renda bruta do vendedor {quantidade_vendedores}º? '))
    salarios.append(salario)

posicao = [0] * 9

def calcular_posicao(salario):
    valor_recebido = min(math.ceil((salario - 200) / 100))
    return valor_recebido


for i in salarios:
    vendas = 200 + 0.09 * i
    lugar = calcular_posicao(vendas)
    posicao[lugar - 1] += 1


for i in range(9):
    if i == 8:
        print(f'$1000 em diante: {posicao[i]} vendedores')
    else:
        print(f'${(i + 1) * 100 + 100} - ${(i + 1) * 100 + 199}: {posicao[i]} vendedores')