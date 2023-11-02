# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do produto? '))
desconto = preço - (preço * 5 / 100)

print(f'O produto que custava R${preço}, promoção com desconto de 5% vai custar R${desconto:.2f}')