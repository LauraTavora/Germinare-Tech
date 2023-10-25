estoque = {
    1: "Camiseta",
    2: "Calça",
    3: "Camiseta",
    4: "Tênis",
    5: "Calça"
}


def inverter_estoque(estoque):
    estoque_invertido = {}
    
    for codigo, nome in estoque.items():
        if nome not in estoque_invertido:
            estoque_invertido[nome] = []
            
        estoque_invertido[nome].append(codigo)
    
    return estoque_invertido


estoque_invertido = inverter_estoque(estoque)
print(estoque_invertido)