# Função para calcular o valor da dívida após um pagamento mensal
def calcular_divida(devedor, pagamento_mensal):
    # Verifica se a dívida já foi totalmente paga
    if devedor <= 0:
        return 0, 0
    # Calcula o valor da dívida após o pagamento mensal
    if pagamento_mensal >= devedor:
        devedor -= devedor  # Cliente pagou o valor total da dívida
        return 0, devedor
    else:
        devedor -= pagamento_mensal
        return pagamento_mensal, devedor

# Função principal
def principal():
    # Solicita o valor total da dívida e o pagamento mensal ao usuário
    valor_divida = float(input("Informe o valor total da dívida: "))
    pagamento_mensal = float(input("Informe o valor do pagamento mensal: "))

    # Loop para acompanhar o pagamento mensal
    mes = 1
    while valor_divida > 0:
        pagamento, valor_divida = calcular_divida(valor_divida, pagamento_mensal)
        print(f"Mês {mes}: Pagamento de R${pagamento:.2f}, Dívida restante: R${valor_divida:.2f}")
        mes += 1

    print("Dívida totalmente paga!")

if __name__ == "__principal__":
    principal()
