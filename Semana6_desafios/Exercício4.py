while True:
    aplicacao = float(input('Digite o valor da aplicação: '))
    if aplicacao < 2000:
        print('Aplicação Inválida. Digite um valor de R$2000,00 para cima')
        break
        

    meses = int(input('Por quantos meses durará a aplicação: '))
    if aplicacao <= 2000:
        taxa_juros = 0.005  
    elif aplicacao >= 2000 and aplicacao <= 10000:
        taxa_juros = 0.01  
    else:
        taxa_juros = 0.015  


    aplicacao_juros = aplicacao * (1 + taxa_juros) ** meses
    print(f'O valor recebido será de R${aplicacao_juros:.2f} ')

    parada = input('Você quer fazer o cálculo de outro resgate? ')
    if parada.lower() != 's':
        break
