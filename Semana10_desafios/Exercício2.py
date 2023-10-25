conta = {
    'transações': 0, 
    'saldo': 1000, 
    'média': 0
}

def compra(conta, valor):
    conta['transações'] += 1

    conta['saldo'] -= valor

    media = (conta['média'] * (conta['transações'] - 1) + valor) / conta['transações']
    conta['média'] = media

    return conta


conta = compra(conta, 100)
conta = compra(conta, 200)

print(conta)