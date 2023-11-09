#GRUPO 7 - HACKATHON
#MEMBROS:
#Clara Bartolini Moreira, Laura Francisco Távora, Bruno Guedes Galvão, Luan Henrique Natell de Souza, Sofia Bonini Pinto, Liane Thiemi Thinen Isoda, Natália Trindade Dos Santos, Giovanna Pereira Da Rosa Rosa Nascimento, Samuel Evangelista Mauricio, Marianne Gonçalves Feitosa, Manuelli Reis Sá Flaviano, João Pedro Carvalho De Jesus

from time import sleep
from fpdf import FPDF
import requests

selic = 12.75

class color:
    azul = '\033[94m'
    verde = '\033[92m'
    amarelo = '\033[93m'
    vermelho = '\033[91m'
    negrito = '\033[1m'
    sublinhado = '\033[4m'
    normal = '\033[0;0m'

dy = requests.get("https://raw.githubusercontent.com/germinatech/base_hackathon/main/dy.json")
dy = dy.json()
ativos = requests.get("https://raw.githubusercontent.com/germinatech/base_hackathon/main/ativos.json")
ativos = ativos.json()

def inputEscolhaMenu(entrada):
    while True:
        num = input(entrada)
        if num.isnumeric() and 1 <= int(num) <= 3:
            return int(num)
        else:
            print('Digite uma escolha válida! (1, 2 ou 3)')


def menu(ativos):

    nome = str(input('Digite seu nome completo: '))
    data_nascimento = input('Digite sua data de nascimento ([dia/mes/ano]):  ')
    print('''Qual é seu perfil investidor:
        1- Conservador:Esse tipo de investidor dá mais importância para segurança e liquidez, ou seja, escolhe opções de baixo risco
        2- Moderado: Esse tipo de investidor mantém forte intersse pela segurança, porém está disposto a abrir mão dela para retornos melhores
        3- Arrojado: Esse tipo de investidor é caracterizado por investimento com maior probabilidade de correr riscos, isso em troca de resultados financeiros mais rápidos  '''
        )

    escolha = inputEscolhaMenu('Qual é seu perfil de investidor? ')

    if escolha == 1:
        print(f''' Os ativos indicados são:
              -{ativos[2]}
              -{ativos[3]}
              Segmentos indicados: 
                -Fundo de investimentos imobiliários
                -Ação de saúde
                -Ação de energia''')
    elif escolha ==2:
        print(f''' os ativos indicados são:
              -{ativos[0]}
              Segmentos indicados:
                -Ação de alimentos
''')
    else: 
        print(f''' Os ativos indicados são:
                -{ativos[1]} 
            Segmentos indicados:
                -Ação de varejo''')

menu(ativos)

segMGLU3_SA ={}
segJBSS3_SA ={}
segMRFG3_SA ={}
segTAEE3_SA ={}
segFLRY3_SA ={}
segHGLG11_SA  ={}
segLREN3_SA ={}
segRDOR3_SA  ={}
segTRPL3_SA ={}
segXPLG11_SA ={}

x = {"JBSS3.SA": 8.15, "MRFG3.SA": 6.8, "MGLU3.SA": 1.44, "TAEE3.SA": 7.1, "FLRY3.SA": 2, "HGLG11.SA": 9.15, "LREN3.SA": 8.98, "RDOR3.SA": 5.15, "TRPL3.SA": 1.31, "XPLG11.SA": 10.31}
conservador = []
moderado = []
arrojado = []
energia = []
varejo= []
alimento = []
saude = []
imobiliaria= []
for i in ativos:
    if i['segmento'] == "Saude":
        saude.append(i)
        conservador.append(i)
    elif i['segmento'] == "Energia":
        energia.append(i)
        conservador.append(i)
    elif i['segmento'] == "Alimento":
        moderado.append(i)
        alimento.append(i)
    elif i['segmento'] == "Varejo":
        varejo.append(i)
        arrojado.append(i)
    elif i['segmento'] == "FII":
        imobiliaria.append(i)
        conservador.append(i)

JBSS3_SA = []
MRFG3_SA = []
MGLU3_SA = []
TAEE3_SA = []
FLRY3_SA= []
HGLG11_SA = []
LREN3_SA = []
RDOR3_SA = []
TRPL3_SA = []
XPLG11_SA = []

for i in ativos:
    if i['ticker'] == "JBSS3.SA":
        JBSS3_SA.append(i)
        for b in JBSS3_SA:
           segMJBSS3_SA = {b['segmento']}
    if i['ticker'] == "MRFG3.SA":
        MRFG3_SA.append(i)
        for b in MRFG3_SA:
           segMRFG3_SA = {b['segmento']}
    if i['ticker'] == "TAEE3.SA":
        TAEE3_SA.append(i)
        for b in TAEE3_SA:
           segTAEE3_SA = {b['segmento']}
    if i['ticker'] == "FLRY3.SA":
        FLRY3_SA.append(i)
        for b in FLRY3_SA:
           segFLRY3_SA = {b['segmento']}
    if i['ticker'] == "JHGLG11.SA":
        HGLG11_SA.append(i)
        for b in HGLG11_SA:
           segHGLG11_SA= {b['segmento']}
    if i['ticker'] == "LREN3.SA":
        LREN3_SA.append(i)
        for b in LREN3_SA:
           segLREN3_SA= {b['segmento']}
    if i['ticker'] == "RDOR3.SA":
        RDOR3_SA.append(i)
        for b in RDOR3_SA:
           segRDOR3_SA = {b['segmento']}
    if i['ticker'] == "TRPL3.SA":
        TRPL3_SA.append(i)
        for b in TRPL3_SA:
           segTRPL3_SA = {b['segmento']}
    if i['ticker'] == "XPLG11.SA":
        XPLG11_SA.append(i)
        for b in XPLG11_SA:
           segXPLG11_SA = {b['segmento']}
    if i['ticker'] == "MGLU3.SA":
        MGLU3_SA.append(i)
        for b in MGLU3_SA:
           segMGLU3_SA = {b['segmento']}

print(segMGLU3_SA,
segJBSS3_SA,
segMRFG3_SA,
segTAEE3_SA,
segFLRY3_SA,
segHGLG11_SA,
segLREN3_SA,
segRDOR3_SA ,
segTRPL3_SA,
segXPLG11_SA)

print(dy)

dytotais = []

for a in dy.values():
    dytotais.append(a)

dydecrescente = sorted(dytotais)
maiordy = dytotais[len(dytotais) - 1]
print(maiordy)

for k, v in dy.items():
    if v == maiordy:
        nomemaiordy = k

#print(nomemaiordy)


# conservador = []
# moderado = []
# arrojado = []
# energia = []
# varejo= []
# alimento = []
# saude = []
# imobiliaria= []

# for i in ativos:
#     if i['segmento'] == "Saude":
#         saude.append(i)
#         conservador.append(i)
#     elif i['segmento'] == "Energia":
#         energia.append(i)
#         conservador.append(i)
#     elif i['segmento'] == "Alimento":
#         moderado.append(i)
#         alimento.append(i)
#     elif i['segmento'] == "Varejo":
#         varejo.append(i)
#         arrojado.append(i)
#     elif i['segmento'] == "FII":
#         imobiliaria.append(i)
#         conservador.append(i)

def comparacao(selic, val):
    if val == selic:
        print("Eles são iguais.")

    elif val < selic:
        print(f"O valor {val} é menor que o selic.")

    elif val > selic:
        print(f"O valor {val} é maior que o selic")

    return val

jbsdesempenho = 14.32
magazinedesempenho = -54,94


def gerandoPDF():
    pdf = FPDF() #Essa linha cria uma variável que vai armazenar as informações da função FPDF da bibliotec
    pdf.add_page() #Essa linha cria uma página em PDF, em branco ainda.
    pdf.set_font("Arial", size=20) #Essa linha é definida que os textos irão aparecer na fonte Arial e no tamanho de 20pt (lembra do word? igual.)
    # pdf.image('imagem.png', x = None, y = None, w = 200, h = 200) # Essa linha é para adicionar uma imagem, é uma função, observe, abaixo vou explicar cada posiçõa:
    """
    'imagem.png' -> é o arquivo de imagem que você quer adicionar no seu PDF
    x = None -> isso é o deslocamento na horizontal (para direita ou esquerda), se você colocar None a imagem vai ficar à esquerda.
    y = None -> isso é o deslocamento na vertical (de cima para baixo), se colocar None a imagem vai ficar no canto superior do PDF
    w = 200 -> isso é a Width, ou Largura da imagem
    h = 200 -> isso é a Height, ou altura da imagem
    #OBS: O arquivo deve esta na mesma pasta onde você ta criando o seu código em python, observe se a imagem está aparecendo no explorador à esquerda no VScode.
    """
    cont = 0
    #abaixo vou criar uma string que vai aparecer no PDF:
    recomendacaoarrojado = [f'As recomendações de cada segmento pro perfil arrojado são: ',
                f'Segmento Varejo: Carrefour e Magazine Luiza',
                f'Segmento Energia: Auren, CPFL',
                f'Segmento Saúde: Fleury, Biomm',
                f'Segmento Alimentos: JBS',
                f'Fundo Imobiliário: Fundos de Recebíveis Imobiliários',
    ]

    recomendacaomoderado = [f'As recomendações pro perfil moderado são: ',
                f'Segmento Alimentos: Brasil Agro, Agrogalaxy',
                f''
    ]

    recomendacaoconservador = [f'As recomendações pro perfil conservador são: ',
                               f'Ativo com maior DY: {nomemaiordy}'
    ]


    comparacao(selic, maiordy)


    comparativoindicacoes = [f'Comparativo das indicações com a SELIC: ',    
                             f'Alimento: {comparacao(selic, jbsdesempenho)}',]




    for i in range(0,len(recomendacaoarrojado)):
        pdf.cell(100, 10, txt=str(recomendacaoarrojado[i]), ln=100, align='L')

    for i in range(0,len(recomendacaomoderado)):
        pdf.cell(100, 10, txt=str(recomendacaomoderado[i]), ln=100, align='L')

    for i in range(0, len(recomendacaoconservador)):
        pdf.cell(100, 10, txt=str(recomendacaoconservador[i]), ln=100, align='L')

    for i in range(0,len(comparativoindicacoes)):
        pdf.cell(100, 10, txt=str(comparativoindicacoes[i]), ln=100, align='L')
        
        
    """
    Explicando as linhas de cima:
    pdf.cell() é para adicionar linhas (ou células) no nosso arquivo PDF.
    100 é a largura de cada linha,
    10 é a altura
    txt = str(mensagem[cont]) é para pegar a linha correspondente da variável mensagem e adicionar no pdf
    align='L' é para o texto ficar alinhado à esquerda (LEFT)
    Tente entender porque foi usado o WHILE e como?
    """
    # pdf.image('outra_imagem.png', x = None, y = None, w = 100, h = 50)
    #Na linha acima o que foi feito? Adicionado outra imagem depois do texto.
    pdf_name = "grupo7relatorio.pdf" # aqui definimos o nome do arquivo que vai ser gerado
    pdf.output(pdf_name) #aqui o arquivo é criado na mesma pasta onde você está trabalhando.
    
    print(f'O pdf {pdf_name} foi criado com sucesso')

gerandoPDF()