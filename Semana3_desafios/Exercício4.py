import datetime
from datetime import datetime # --> usado para não ter que ficar colocando os nomes das bibliotecas.

primeira_data = input('Digite sua data de nascimento no formato "ano-mês-dia":')
segunda_data = input('Digite a data de nascimento do seu amigo no formato "ano-mês-dia":')

def calcular_diferenca_idade(primeira_data, segunda_data):
    #(strptime) é usado para formartar objetos de data em strings legíveis
    primeira_data = datetime.strptime(primeira_data, "%Y-%m-%d")
    segunda_data = datetime.strptime(segunda_data, "%Y-%m-%d")

    diferenca = primeira_data - segunda_data

    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    
    return anos, meses, dias 

calculando_anos, calculando_meses, calculando_dias = calcular_diferenca_idade(primeira_data, segunda_data)

print(f'A diferença de idade entre vocês é de: {calculando_anos} anos, {calculando_meses} meses, {calculando_dias} dias.')