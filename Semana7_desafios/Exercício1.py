def comprando_imovel():
    valor_imovel = int(input('Qual o valor do imóvel? '))
    investimento_mensal = int(input('Qual será o investimento mensal fixo? '))
    juro_mensal = int(input('Qual é a taxa mensal de juros? '))

    juros_decimal = juro_mensal / 100
    porcentagem_imovel = 0.01 * valor_imovel

    
    if investimento_mensal < porcentagem_imovel:
        print('Seu investimento não é viável')
        return
    
    conta = 0
    meses = 0

    for conta in range(conta < valor_imovel):
        conta += investimento_mensal
        conta *= (1 + juros_decimal)
        meses += 1

    #while conta < valor_imovel:
        #conta += investimento_mensal
        #conta *= (1 + juros_decimal)
        #meses += 1
            
    print(f'O tempo necessário para comprar esse imóvel é {meses:.0f} meses')


comprando_imovel()
        