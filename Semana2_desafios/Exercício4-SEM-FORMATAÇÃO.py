populacao_inicial = float(input('Digite a população inicial:').replace(".", ""))
taxa_crescimento = float(input('Digite a taxa de crescimento anual em decimais:').replace(",",""))
anos = int(input('Digite o intervalo de anos:'))

populacao_final = populacao_inicial * (1 + taxa_crescimento)* anos 


print(f"A população após {anos} anos será de {populacao_final:.0f} habitantes.")