base = int(input('Base do retângulo:'))
altura = int(input('Altura do retângulo:'))
preco_lata = int(input('Digite o preço de cada lata:'))
# Cada lata de tinta contém 5 litros
# Cada litro de tinta pinta 3 metros quadrados
# Ou seja cada lata pode pintar 15 metros quadrados
area = (base * altura) / 15

print(f'A quantidade de latas que devem ser compradas para pintar o quintal é {area:.0f} latas') 
valor = (preco_lata * area)
print(f'O valor total que deverá ser gasto para comprar as latas é de R${valor:.0f} reais')