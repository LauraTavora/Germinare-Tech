funcionarios = []

def cadastrar_funcionario(nome, idade, salario, setor):
    func = {
        'nome': nome,
        'idade': idade, 
        'salario': salario,
        'setor': setor
    }

    funcionarios.append(func)

cadastrar_funcionario('Marcelo Grilo', 33, 1500.50, 'Germinare TECH')
cadastrar_funcionario('Larissa Manoela', 15, 2500, 'Germinare TECH')

for f in funcionarios:
    for chave, valor in f.items():
        if f['nome'] == 'Larissa Manoela':
            print(f'{chave} = {valor}')