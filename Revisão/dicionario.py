# Cria um dicionário vazio para armazenar os usuários
usuarios = {}

def cadastrar_usuario():
    while True:
        nome = input("Digite o nome completo do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        cpf = input("Digite o CPF do usuário: ")
            
        usuarios[cpf] = {
            'nome': nome,
            'idade': idade,
            'cpf': cpf
        }
        print("Usuário cadastrado com sucesso!")


def remover_usuario():
    cpf = input("Digite o CPF do usuário que deseja remover: ")
    if cpf in usuarios:
        del usuarios[cpf]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")
        adicionar_usuario = input('Deseja cadastrar esse usuário? (S/N) ').upper()
        if adicionar_usuario == 'S':
            cadastrar_usuario()
    

def alterar_usuario():
    cpf = input("Digite o CPF do usuário que deseja alterar: ")
    if cpf in usuarios:
        nome = input("Digite o novo nome completo do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        
        usuarios[cpf]['nome'] = nome
        usuarios[cpf]['idade'] = idade
        print("Informações do usuário alteradas com sucesso!")
    else:
        print("Usuário não encontrado.")
        adicionar_usuario = input('Deseja cadastrar esse usuário? (S/N) ').upper()
        if adicionar_usuario == 'S':
            cadastrar_usuario()

def buscar_usuario():
    cpf = input("Digite o CPF do usuário que deseja buscar: ")
    if cpf in usuarios:
        usuario = usuarios[cpf]
        print(f'Nome: {usuario["nome"]}')
        print(f'Idade: {str(usuario["idade"])}')
        print(f'CPF: {usuario["cpf"]}')
            # Outra forma de fazer:
            #print('Nome: ' + usuario['nome'])
            #print("Idade: " + str(usuario['idade']))
            #print("CPF: " + usuario['cpf'])
    else:
        print("Usuário não encontrado.")
        adicionar_usuario = input('Deseja cadastrar esse usuário? (S/N) ').upper()
        if adicionar_usuario == 'S':
            cadastrar_usuario()

def mostrar_usuarios():
    if not usuarios:
        print('Não há nenhum usuário cadastrado!')
    else:
        print()
        print('==================== Usuários ====================')
        for nome, idade, cpf in usuarios.items():
            print(f'Nome - {nome}')
            print(f'Idade - {idade}')
            print(f'CPF - {cpf}')
            print('==============================================')
            print()

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar usuário")
    print("2. Remover usuário")
    print("3. Alterar informações de usuário")
    print("4. Buscar usuário")
    print("5. Mostrar usuários cadastrados")
    print("6. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        remover_usuario()
    elif opcao == "3":
        alterar_usuario()
    elif opcao == "4":
        buscar_usuario()
    elif opcao == "5":
        mostrar_usuarios()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
