funcionarios = {
    'Marcelo Grilo':{
        'idade': 33,
        'salario': 1500.50,
        'setor': 'Germinare TECH'
    },
    'Larissa Manoela':{
        'idade': 15,
        'salario': 2500,
        'setor': 'Germinare TECH'
    }
}

for chave, valor in funcionarios.items():
    for item, valor_item in valor.items():
        print(f'Funcionário {chave} - {item}= {valor_item}')