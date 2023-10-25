agenda = {}

def incluirNovoTel():
    while True:
        nome = str(input('Digite o nome: '))
        telefone = int(input('Digite o número de telefone: '))

        while telefone < 9:
            print('Telefone Inválido. Digite-o novamente')
            telefone = int(input('Digite o número de telefone: '))

        if nome in agenda:
            agenda[nome].append(telefone)
        else:
            agenda[nome] = [telefone]

        break


def incluirTelefone():
    while True:
        nome = input('Qual o nome para acrescentar o número? ')
        if nome in agenda:
            numero = int(input('Digite o número desejado: '))
            agenda[nome].append(numero)
        else:
            print('O nome não encontrado na lista')
            adicionar_nome = input('Deseja adicionar esse nome? ').upper()
            if adicionar_nome == 'S':
                incluirNovoTel()
        
        break

def excluirTelefone():
    while True:
        nome = input('Qual o nome para excluir o número? ')
        if nome in agenda:
            numeros = agenda[nome]
            print(f'Números de {nome} disponíveis para excluir:')
            if len(numeros) == 1:
                del agenda[nome]
                print(f'O nome {nome} foi removido da lista, por ter apenas um número de telefone.')
            else:
                posicao = 0
                while posicao < len(numeros):
                    print(f'Posição {posicao} - Número {numeros[posicao]}')
                    posicao += 1
                numero = int(input('Digite a posição do número que deseja excluir: '))
                if 0 <= numero < len(agenda[nome]):
                    del numeros[numero]
                    print(f'O número foi excluído da lista de {nome}.')
                else:
                    print('Número inválido')
        else:
            print('O nome não foi encontrado na lista')
            adicionar_nome = input('Deseja adicionar esse nome? ').upper()
            if adicionar_nome == 'S':
                incluirNovoTel()
       
        break

def excluirNome():
    nome = input('Qual o nome de quem você deseja excluir? ')
    if nome in agenda:
        del agenda[nome]
        print(f'O nome {nome} foi excluído da lista.')
    else:
        print('O nome não foi encontrado na lista.')
        adicionar_nome = input('Deseja adicionar esse nome? ').upper()
        if adicionar_nome == 'S':
            incluirNovoTel()

def mostrarAgenda():
    if not agenda:
        print('A agenda está vazia.')
    else:
        print()
        print("====================Agenda de Contatos====================")
        for nome, telefones in agenda.items():
            print(f'Nome - {nome}')
            print('Telefones:')
            for telefone in telefones:
                print(f'  - {telefone}')
            print('====================================================')
            print()

while True:
    opcao = input('Escolha uma opção:\n1. Incluir novo nome e telefone;\n2. Incluir telefone a um nome existente;\n3. Excluir telefone de um nome;\n4. Excluir nome;\n5. Mostrar agenda;\n6. Sair.\nOpção: ')
    
    if opcao == '1':
        incluirNovoTel()
    elif opcao == '2':
        incluirTelefone()
    elif opcao == '3':
        excluirTelefone()
    elif opcao == '4':
        excluirNome()
    elif opcao == '5':
        mostrarAgenda()
    elif opcao == '6':
        break
    else:
        print('Opção inválida. Escolha novamente.')
