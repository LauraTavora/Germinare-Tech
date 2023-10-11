produtos = ('Pão de queijo 400g','Salsicha Hot-dog 500g','Pão de alho baguete 400g',
            'Filé de Peito de Frango 1Kg','Isca de Frango 300g','Linguiça toscana 700g',
            'Pedaço de Filé de Salmão 500g','Filé de Tilápia 250g',
            'Bife de Filé Mignon MAIS 900g','Carne moída patinho')

precos =  (10.76,9.96,10.96,19.96,13.96,17.96,54.96,13.96,89.96,39.97)


print('========================= MENU =========================')
def mostrar_menu(produtos,precos):
    print('Produtos........................................Precos')
    for precos, produtos in zip(precos, produtos):
        tamanho = 47 - len(produtos)
        print(f'{produtos} {"." * tamanho}R${precos:.2f}')

mostrar_menu(produtos, precos)
print('=' * 56)

print()
print()
print('=============================== PRODUTOS ===============================')

def caro_e_barato():
    caro = max(precos)
    produto_caro = precos.index(caro)
    nome_caro = produtos[produto_caro]

    barato = min(precos)
    produto_barato = precos.index(barato)
    nome_barato = produtos[produto_barato]

    #Index -> Usado para descobrir o indice de um elemento da tupla

    print(f'O produto mais caro é {nome_caro} no valor de R${caro:.2f}')
    print(f'O produto mais barato é {nome_barato} no valor de R${barato:.2f}')

print()
caro_e_barato()



def soma(soma):
    soma = sum(precos)
    print(f'A soma de todos os produtos é de R${soma:.2f}')

soma(soma)

print()
print('=' * 73)
