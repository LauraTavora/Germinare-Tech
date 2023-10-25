clientes = {
    'Nome': 'Ana Maria Braga',
    'Endereco': 'Av. Maria Augusta,s/n',
    'OperadoraCelular':'Vivo',
    }
valor = 'Maria'


def encontrando_chaves(clientes,valor_analisado):
    chaves_encontradas = []
    for chave, valor in clientes.items():
        if valor_analisado.lower() in valor.lower():
            chaves_encontradas.append(chave)
    
    return ', '.join(chaves_encontradas)

print(encontrando_chaves(clientes,valor))