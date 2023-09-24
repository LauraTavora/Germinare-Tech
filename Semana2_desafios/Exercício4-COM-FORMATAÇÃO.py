def formato_ibge(number):
    partes = "{:,.0f}".format(number).split(",")
    numero_formatado = ".".join(partes)
    return numero_formatado


populacao_inicial = float(input('Digite a população inicial:').replace(".", ""))
taxa_crescimento = float(input('Digite a taxa de crescimento anual em decimais:').replace(",",""))
anos = int(input('Digite o intervalo de anos:'))

populacao_final = populacao_inicial * (1 + taxa_crescimento)* anos 

valor_saida = formato_ibge(populacao_final)

print(f"A população após {anos} anos será de {valor_saida} habitantes.")