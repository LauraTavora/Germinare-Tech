quantidade_produtos = int(input('Quantos produtos você deseja pegar? '))
s = 0
while True:
    if quantidade_produtos <= 0:
        print('Número de produtos inválidos. Coloque uma quantidade maior que 0')
        break
    for i in range(0, quantidade_produtos):
        valor = float(input('Valor do produto: '))
        if valor <= 0:
            print('Preço dos produtos inválidos. Coloque um valor maior que 0')
        s += valor
    
    if s < 100:
        print(f'O valor total da compra é: R${s:.2f} ')
        print('Não terá um valor de desconto, pois o valor total da compra foi menor que 100')
    else:

        if quantidade_produtos == 4:
            desconto_aplicado = ((4*s)/100) 
            valor_desconto_pagar = s - desconto_aplicado
            print(f'O valor total da compra sem desconto é: R${s:.2f} ')
            print('O percentual de desconto é igual a 4%')
            print(f'O valor de desconto foi: R${desconto_aplicado:.2f}')
            print(f'O valor total da compra com desconto é: R${valor_desconto_pagar:.2f} ')
        elif quantidade_produtos == 5:
            desconto_aplicado = ((8*s)/100) 
            valor_desconto_pagar = s - desconto_aplicado
            print(f'O valor total da compra sem desconto é: R${s:.2f} ')
            print('O percentual de desconto é igual a 8%')
            print(f'O valor de desconto foi: R${desconto_aplicado:.2f}')
            print(f'O valor total da compra com desconto é: R${valor_desconto_pagar:.2f} ')
        elif quantidade_produtos >= 6:
            desconto_aplicado = ((12*s)/100) 
            valor_desconto_pagar = s - desconto_aplicado
            print(f'O valor total da compra sem desconto é: R${s:.2f} ')
            print('O percentual de desconto é igual a 12%')
            print(f'O valor de desconto foi: R${desconto_aplicado:.2f}')
            print(f'O valor total da compra com desconto é: R${valor_desconto_pagar:.2f} ')
        else:
            print(f'O valor total da compra sem desconto é: R${s:.2f}')
            print('Devido ao número de produtos, não terá um percentual de desconto')
            print('O valor de desconto foi: R$0.00')
            print(f'O valor total da compra com desconto é: R${s:.2f}')

    break

print('FIM')