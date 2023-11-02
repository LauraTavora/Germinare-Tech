codigos = [102,204,305,400,401,500]
precos = [10.96, 13.96, 17.96, 54.96, 13.96, 89.96]
estoques = [4, 0, 75, 1, 2, 5]

def menu():
    print("\x1b[2J")  #print acima é para limpar a tela do terminal
    print(f'\033[1;33mCódigo --|--            Produto            --|-- Preço(R$) --|-- Estoque\033[0;0m')
    print(f'\n{codigos[0]:^7}--|--{"Pão de alho baguete 400g":^31}--|--{precos[0]:^11}--|--{estoques[0]:^6}',
    f'\n{codigos[1]:^7}--|--{"Isca de Frango 300g":^31}--|--{precos[1]:^11}--|--{estoques[1]:^6}',
    f'\n{codigos[2]:^7}--|--{"Linguiça toscana 700g":^31}--|--{precos[2]:^11}--|--{estoques[2]:^6}',
    f'\n{codigos[3]:^7}--|--{"Pedaço de Filé de Salmão 500g":^31}--|--{precos[3]:^11}--|--{estoques[3]:^6}',
    f'\n{codigos[4]:^7}--|--{"Filé de Tilápia 250g":^31}--|--{precos[4]:^11}--|--{estoques[4]:^6}',
    f'\n{codigos[5]:^7}--|--{"Filé de Tilápia 250g":^31}--|--{precos[5]:^11}--|--{estoques[5]:^6}'
    f'\n\033[1;31m{999:^7}---->{"FINALIZAR O PROGRAMA":^31}\033[0;0m'
    )

menu()

def validar_codigo(codigos):
    items_comprados = 0
    codigos_produtos = []
    precos_produtos = 0
    codigos.append(999)
    while True:
        codigo_compra = int(input('Digite o código do produto desejado: '))
        
        if codigo_compra in codigos:
            index_codigos = codigos.index(codigo_compra)
            if estoques[index_codigos] == 0:
                print('Produto sem estoque. Escolha outro produto')
            else:
                estoques[index_codigos] -= 1
                items_comprados += 1   
                codigos_produtos.append(codigo_compra)  
                precos_produtos += precos[index_codigos]
        else:
            print('Código inválido. Digite um código que aparece no menu')      

        if codigo_compra == 999:
                print(f'A quantidade de produtos comprados foi de: {items_comprados}')
                print(f'Códigos dos produtos comprados: {codigos_produtos}')
                print(f'O valor total da compra foi de R${precos_produtos:.2f}')
                break   

                    


validar_codigo(codigos)