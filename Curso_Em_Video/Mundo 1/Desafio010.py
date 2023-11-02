# Crie um programa que leia quanto dinherio uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Obs: Considere US$1,00 = R$3,27

reais = float(input('Quanto de dinheiro você tem na carteira? R$'))

dolar = reais / 3.27

print(f'Com R${reais:.2f} você pode comprar US${dolar:.2f}')