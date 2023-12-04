tipo_pizza = []
pizza = []
refrigerante = []


def sabor_pizza():
    print('''Opções de sabores de pizza:
1. Mussarela
2. Calabresa
3. Frango com Catupiry''')
    escolha = int(input('Escolha um sabor (1/2/3): '))
    if escolha == 1:
        tipo_pizza.append('Mussarela')
    if escolha == 2: 
        tipo_pizza.append('Calabresa')
    if escolha == 3:
        tipo_pizza.append('Frango com Catupiry')

def tamanho_pizza():
   print(''' Opções de tamanho de pizza:
1. Pequena
2. Média
3. Grande''')
   escolha = int(input('Escolha um tamanho (1/2/3): '))
   if escolha == 1:
       pizza.append('Pequena')
   if escolha == 2:
       pizza.append('Média')
   if escolha == 3:
       pizza.append('Grande')

def adicionando_refri():
    adicionar_refri = str(input('Deseja adicionar refrigerante (S/N)? ')).upper()
    if adicionar_refri == 'S':
        refrigerante.append('adicionado')
    else:
        refrigerante.append('não adicionado')

def resumo_pedido():
    print(f'''Resumo do pedido:
Sabor da pizza: {tipo_pizza}
Tamanho da pizza: {pizza}
Refrigerante {refrigerante} ao pedido''')
    


while True:
    opcao = input('Escolha uma opção:\n1. Escolher sabor de pizza\n2. Escolher tamanho de pizza\n3. Adicionar refrigerante\n4. Finalizar pedido\nEscolha uma opção: ')
    
    if opcao == '1':
        sabor_pizza()
    elif opcao == '2':
        tamanho_pizza()
    elif opcao == '3':
        adicionando_refri()
    elif opcao == '4':
        resumo_pedido()
        break
    else:
        print('Opção inválida. Escolha novamente.')
