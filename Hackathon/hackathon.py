# HACKATHON - 28/10/2023
# OBJETIVO: Seu objetivo é criar um programa em Python que analise dados históricos de 10 ativos financeiros nos últimos 6 meses e forneça recomendações de investimento com base em análises e métricas financeiras.

                      # Primeiro Passo: Entender os conceitos essenciais relacionados a investimentos.

# ATIVOS FINANCEIROS: Produtos disponíveis no mercado financeiro e de capitais para serem negociados.
# BOLSA DE VALORES: A bolsa de valores é um ambiente onde são negociados ações, títulos e outros ativos. A bolsa funciona como um ponto de encontro entre empresas e investidores.
# ABERTURA E FECHAMENTO DE MERCADO: A abertura/fechamento do mercado é o inicio e o fim da bolsa de valores(B3) no dia.
# DIVIDEND YIELD(DY): O dividend yield é um indicador que mede o rendimento de uma ação apenas com o pagamento de dividendos.
# SELIC: A Selic, ou Taxa Selic, é a taxa básica de juros da economia brasileira. A cada 45 dias ela pode sofrer alguma alteração, ou seja, aumentar, diminuir ou se manter estável, após a tradicional reunião do Copom, o Comitê de Política Monetária do Banco Central.
# INFLAÇÃO: Inflação é o nome dado ao aumento dos preços de produtos e serviços. Ela é calculada pelos índices de preços, comumente chamados de índices de inflação.
################################################################################################################################################

import requests
from fpdf import FPDF
from time import sleep

class color:
    azul = '\033[94m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    vermelho = '\033[91m'
    negrito = '\033[1m'
    sublinhado = '\033[4m'
    normal = '\033[0;0m'

ativos = requests.get('https://github.com/germinatech/base_hackathon/blob/main/ativos.json')
ativos.json()

dy = requests.get('https://github.com/germinatech/base_hackathon/blob/main/dy.json')
dy.json()

selic = 12.75
inflação = 5.19


def menu():
    print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=MENU PERFIL DE INVESTIDOR-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
1- Conservador: O investidor conservador está disposto a renunciar a rentabilidade em troca de mais segurança.
2- Moderado: O investidor moderado possui tolerância a riscos de longo prazo, sendo assim ele escolhe por investimentos mais arriscados dependendo da situação:
3- Arrojado: O investidor arrojado, assume riscos em busca de altos rendimentos, foca o longo prazo e corre riscos calculados
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= ''')
    nome = str(input('Digite seu nome completo: '))
    data_nascimento = input('Digite sua data de nascimento (dia/mês/ano): ')
    escolha = int(input('Digite sua escolha para o perfil de investidor: '))
    while escolha != 1 and escolha != 2 and escolha != 3:
            print('Escolha inválida. Digite um valor válido (1,2,3)')
            continue

    
menu()