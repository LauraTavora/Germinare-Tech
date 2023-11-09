nomes = ["Pão de Queijo", "Coxinha", "Esfiha de Carne", "Empada de Frango", "Refrigerante","Suco de Laranja", "Café expresso", "Chocolate Quente", "Água mineral"]
valor = [3.50, 5.00, 5.50, 5.50, 6.00, 8.00, 3.00, 4.50, 2.50]
codigos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def cardapio():
    print("\x1b[2J")  # Print para limpar a tela do terminal
    print(f'\033[1;33mCódigo --|--            Produto            --|-- Valor(R$)\033[0;0m')
    print(f'\n{codigos[0]:^7}--|--{nomes[0]:^31}--|-- R${valor[0]:^5.2f}',
    f'\n{codigos[1]:^7}--|--{nomes[1]:^31}--|-- R${valor[1]:^5.2f}',
    f'\n{codigos[2]:^7}--|--{nomes[2]:^31}--|-- R${valor[2]:^5.2f}',
    f'\n{codigos[3]:^7}--|--{nomes[3]:^31}--|-- R${valor[3]:^5.2f}',
    f'\n{codigos[4]:^7}--|--{nomes[4]:^31}--|-- R${valor[4]:^5.2f}',
    f'\n{codigos[5]:^7}--|--{nomes[5]:^31}--|-- R${valor[5]:^5.2f}'
    f'\n\033[1;31m{0:^7}---->{"FINALIZAR O PROGRAMA":^31}\033[0;0m'
    )

cardapio()

def calcular_item(valor_unitario, quantidade):
    valor_total = valor_unitario * quantidade
    return valor_total

itens_escolhidos = []
quantidades = []
valor_total = 0

while True:
    escolha = int(input('Digite o número do item desejado: '))

    if escolha == 0:
        break 

    if escolha in codigos:
        index_codigos = codigos.index(escolha)
        quantidade = int(input(f'Quantidade de {nomes[index_codigos]}: '))
        itens_escolhidos.append(nomes[index_codigos])
        quantidades.append(quantidade)
        valor_item = calcular_item(valor[index_codigos], quantidade)
        valor_total += valor_item
    else: 
        print('Item inválido. Digite um número que esteja no cardápio.')


print()
for i in range(len(itens_escolhidos)):
    codigo_item = codigos[nomes.index(itens_escolhidos[i])]
    print(f'{quantidades[i]} - {itens_escolhidos[i]} - R${quantidades[i] * valor[codigo_item - 1]:.2f}')
print(f'Valor total da compra: R${valor_total:.2f}')

