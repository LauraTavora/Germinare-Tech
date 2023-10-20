clientes = [
    ('Alice', 30, 'São Paulo', 500),
    ('Bob', 25, 'Rio de Janeiro', 300),
    ('Carol', 35, 'São Paulo', 700),
    ('David', 40, 'Brasília', 1000),
    ('Eva', 28, 'Rio de Janeiro', 400),
]

minimo_idade = 25
maximo_idade = 30
localizacao_desejada = 'Brasília'
valor_compras = 500

def filtrando_clientes(clientes, minimo_idade, maximo_idade, localizacao_desejada, compras):
    clientes_idade = []
    clientes_localizacao = []
    clientes_compras = []

    for cliente in clientes:
        nome, idade, localizacao, compras = cliente

        if minimo_idade <= idade and idade <= maximo_idade:
            clientes_idade.append(cliente)
        if localizacao == localizacao_desejada:
            clientes_localizacao.append(cliente)
        if compras >= valor_compras:
            clientes_compras.append(cliente)

    return clientes_compras, clientes_localizacao, clientes_idade

def idade(clientes_idade):
    print(f'Clientes com idade entre {minimo_idade} e {maximo_idade}:')
    print()
    for cliente in clientes_idade:
        nome, idade, localizacao, compras = cliente
        print(f'Nome: {nome}, Idade: {idade}, Localização: {localizacao}, Compras: {compras}')
    print('=' * 70)


def localizacao(clientes_localizacao):
    print(f'Clientes dentro da localização desejada ({localizacao_desejada}):')
    print()
    for cliente in clientes_localizacao:
        nome, idade, localizacao, compras = cliente
        print(f'Nome: {nome}, Idade: {idade}, Localização: {localizacao}, Compras: {compras}')
    print('=' * 70)


def compras(clientes_compras):
    print(f'Clientes com valor em compras maior ou igual a {valor_compras}:')
    print()
    for cliente in clientes_compras:
        nome, idade, localizacao, compras = cliente
        print(f'Nome: {nome}, Idade: {idade}, Localização: {localizacao}, Compras: {compras}')

clientes_compras, clientes_localizacao, clientes_idade = filtrando_clientes(clientes, minimo_idade, maximo_idade, localizacao_desejada, valor_compras)

idade(clientes_idade)
localizacao(clientes_localizacao)
compras(clientes_compras)