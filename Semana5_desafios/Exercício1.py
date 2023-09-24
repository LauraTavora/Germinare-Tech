import datetime
from datetime import datetime

while True:
    salario = float(input('Digite seu salário atual: '))
    if salario >= 1000:
        break
    else:
        print('Seu salário não terá um aumento.')

ano = datetime.now()
ano_atual = ano.year

ano_contrato = int(input('Digite o ano que você foi contratado: '))
if ano_contrato >= 1995:
    if ano_contrato == ano_atual:
        aumento = salario
        print(f'Seu salário atual é de R${aumento:.2f}')
    else:
        # Calcula o número de anos desde a contratação até o ano atual
        anos_passados = ano_atual - ano_contrato

        # Inicializa o percentual de aumento e o salário atual
        percentual_aumento = 1.5  # Percentual de aumento no primeiro ano
        salario_atual = salario

        # Aplica o aumento progressivo enquanto houver anos para considerar
        while anos_passados > 0:
            salario_aumento = salario_atual * (percentual_aumento / 100)
            salario_atual += salario_aumento
            percentual_aumento += 10
            anos_passados -= 1

        # Calcula o percentual de aumento em relação ao salário inicial
        percentual_total_aumento = ((salario_atual - salario) / salario) * 100

        # Exibe o resultado
        print('O salário atual do funcionário é R${:.2f}'.format(salario_atual))
        print('Ele teve um aumento de {:.2f}% em relação ao salário inicial.'.format(percentual_total_aumento))
else:
    print('Seu salário não será aumentado')
