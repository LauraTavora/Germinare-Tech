def debito():
    if cartao_debito == 1:
        'SIM'
    else: 
        'NÃO'


def calculando_preco(tipo_carne, quantidade, cartao_debito):
    preco_kg = 0 
    nome_carne = ''

    if tipo_carne == 1:
        if quantidade <= 5:
            preco_kg += 4.90
        else: 
            preco_kg = 5.80 
        nome_carne += 'File Duplo'
    elif tipo_carne == 2:
        if quantidade <= 5:
            preco_kg += 5.90
        else: 
            preco_kg = 6.80 
        nome_carne += 'Alcatra'
    elif tipo_carne == 3:
        if quantidade <= 5:
            preco_kg += 6.90 
        else:
            preco_kg = 7.80 
        nome_carne += 'Picanha'
    else: 
        print('Tipo de carne inválido.')
        return 
    
    preco_total = quantidade * preco_kg

    if cartao_debito == 1:
        desconto = (preco_total * 0.05)
        preco_desconto = preco_total - desconto
    else: 
        desconto = 0
        preco_desconto = preco_total 

    print('**************CUPOM FISCAL**************')
    print(f'* Carne: {nome_carne}')
    print(f'* Quantidade: {quantidade:.0f}Kg')
    print(f'* Preço: R${preco_total:.2f}')
    print(f'* Cartão de Débito: {debito()}')
    print(f'* Total com desconto: R${preco_desconto:.2f}')
    print('*****************************************')


print('Mercado J&F - Promoção FRIBOI')
print('1 - File Duplo')
print('2 - Alcatra')
print('3 - Picanha')

print('')

tipo_carne = int(input('Digite o tipo que deseja levar:'))
quantidade = float(input('Digite a quantidade comprada (em Kg):'))

print("A Compra será realizada com cartão de débito?")
print("1 - SIM")
print("2 - NÃO")
cartao_debito = int(input("Sua Escolha: "))

print('')

calculando_preco(tipo_carne, quantidade, cartao_debito)