estoque = {
    ('Camiseta', 20.0, 50),
    ('Calça Jeans', 45.0, 30),
    ('Tênis',60.0, 25)
}

pedidos = (
    ('Camiseta', 5)
    ('Calça Jeans', 1)
    ('Tênis',2)
)

estoque_minimo = int(input('Digite o valor do estoque minimo: '))

def atualizando_estoque(estoque, pedidos, estoque_minimo):
    minimo = set()

    for pedido in pedidos:
        produto, quantidade = pedido
        if produto in estoque:
            preco, produto_estoque  = estoque[produto]
            
            if produto_estoque >= quantidade:
                produto_estoque -= quantidade
                estoque[produto] = (preco, produto_estoque)

                if produto_estoque < estoque_minimo:
                    minimo.add(produto)

    print(estoque)
    return minimo 

abaixo_estoque = atualizando_estoque(estoque, pedidos, estoque_minimo)

if abaixo_estoque:
    print("\033[1;31mProdutos com estoque abaixo do mínimo:\033[0;0m")
    for produto in abaixo_estoque:
        print(produto)
else:
    print("\033[1;32mNenhum produto com estoque abaixo do mínimo.\033[0;0m")