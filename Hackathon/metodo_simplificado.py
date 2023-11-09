import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# URL dos dados dos ativos
ativos_url = "https://github.com/germinatech/base_hackathon/ativos.json"
dy_url = "https://github.com/germinatech/base_hackathon/dy.json"

# Baixe os dados e armazene em listas de dicionários
response_ativos = requests.get(ativos_url)
response_dy = requests.get(dy_url)

ativos_data = response_ativos.json()
dy_data = response_dy.json()

# Processamento dos dados
# Vamos assumir que os dados são organizados da seguinte forma:
# ativos_data é uma lista de dicionários com informações de ativos financeiros
# dy_data é um dicionário onde as chaves são tickers e os valores são o DY

# Crie um DataFrame a partir dos dados de ativos
df_ativos = pd.DataFrame(ativos_data)

# Crie um DataFrame a partir dos dados de DY
df_dy = pd.DataFrame.from_dict(dy_data, orient="index", columns=["DY"])
df_dy.reset_index(inplace=True)
df_dy.rename(columns={"index": "ticker"}, inplace=True)

# Agora você pode realizar análises, como calcular a rentabilidade, segmentos com maior rentabilidade, etc.

# Crie um PDF com recomendações
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Recomendações de Investimento", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

# Crie um objeto PDF
pdf = PDF()
pdf.add_page()

# Adicione as recomendações ao PDF
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Recomendações para investidores arrojados:", ln=True)

# Aqui você pode adicionar recomendações com base nas análises que fez

pdf.cell(0, 10, "Recomendações para investidores moderados:", ln=True)
# Adicione recomendações para investidores moderados

pdf.cell(0, 10, "Recomendações para investidores conservadores:", ln=True)
# Adicione recomendações para investidores conservadores

# Salve o PDF
pdf_file_name = "recomendacoes_investimento.pdf"
pdf.output(pdf_file_name)

print(f"Relatório de recomendações gerado em {pdf_file_name}")
