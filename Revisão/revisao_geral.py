# REVISÃO CURSO PYTHON GERMINATECH - PROVA DIA 03/11

# funções
# def nome_funcao(): #sintaxe de criação de uma função
#     #dentro dos parênteses colocamos os parâmetros de entrada
#     # pode ou não RETORNAR um valor
#     print()

# Bibliotecas externas (módolos)
# from random import randint
from operator import itemgetter
import random as aleatorio

# Inicialização do nosso dicionário:
clientes = []
usuarios = {}

#Criação das funções:
def menu():
    print(
        "1 - Cadastrar usuário",
        "\n2 - Remover usuário",
        "\n3 - Buscar usuário",
        "\n4 - Contar usuários",
        "\n5 - Listar usuários",
        "\n0 - Sair"
    )

def validar_opcao(escolha):
    if escolha >= 0 and escolha <= 5:
        return escolha
    else:
        return -1

def cadastrar_usuario(dicionario):
    dicionario = dicionario.copy()
    nome = input("Digite seu nome: ").strip()
    sobrenome = input("Digite seu sobrenome: ").strip()
    dicionario["nome"] = nome.capitalize()+" "+sobrenome.capitalize()
    dicionario["codigo"] = aleatorio.randint(1000,9999)
    clientes.append(dicionario)
    print(f"O usuário {dicionario['nome']} foi cadastrado, e o código é {dicionario['codigo']}")

def quantidade_registros():
    return len(clientes)

def buscar_codigo():
    codigo = int(input("Qual o código que você quer pesquisar? "))
    for item in clientes:
        if item["codigo"] == codigo:
            return (f"Existe o codigo {codigo} no usuário {item['nome']}")  
    
    return ("Não não existe nenhum usuário cadastrado nesse código")    

def remover_usuario(): 
    codigo = int(input("Qual o código que você quer remover? "))
    for indice, item in enumerate(clientes):
        if item["codigo"] == codigo:
            confirmacao = input(f'Tem certeza que deseja remover o usuário {item["nome"]} [s/n]: ')
            if confirmacao.lower() not in ('não', 'n', 'nao'):
                clientes.pop(indice)
                return f"Usuário com código {codigo} foi removido"
            else:
                return "Nenhuma alteração realizada"

    return ("Não não existe nenhum usuário cadastrado nesse código")
    
def mostrar_usuario(dicionario):
    print('Opção 1- Mostar usuários por ordem de cadastro\nOpção 2- Mostar usuários por ordem alfabética\nOpção 3- Mostrar usuários por ordem de código')
    opcao=int(input('Digite a opção escolhida: ')) 
        
    if opcao==1:
       for item in clientes:
        print('Código:',item['codigo'],'-','Nome:',item['nome'])
    if opcao==2:
        alfabetica=sorted(clientes, key=lambda obj: obj["nome"])
        for cliente in alfabetica :
            print(f"Código: {cliente['codigo']} - Nome: {cliente['nome']} ")
        
    if opcao==3:
        ordem=sorted(clientes, key=lambda obj: obj["codigo"])
        for cliente in ordem :
            print(f"Código: {cliente['codigo']} - Nome: {cliente['nome']} ")
        
        
   
        

      
      
      
            
        


# Programa principal (main)

while True:
    menu()
    opcao = (input("Digite sua escolha: "))
    if opcao.isdigit():
        opcao = int(opcao)
        if (validar_opcao(opcao) == -1):
            print("Opção inválida")
            input("Digite ENTER para continuar")

        elif (validar_opcao(opcao) == 0):
            print("Até mais...")
            break

        elif (validar_opcao(opcao) == 1):
            cadastrar_usuario(usuarios)

        
        elif (validar_opcao(opcao) == 4):
            print(f"Você tem {quantidade_registros()} usuários cadastrados no sistema")
        
        elif (validar_opcao(opcao) == 3):
            print(buscar_codigo())

        elif (validar_opcao(opcao) == 2):
            print(remover_usuario())

        elif (validar_opcao(opcao) == 5):
            print(mostrar_usuario(usuarios))
           

    
    else:
        print("Digite um número, não texto")
        input("Digite ENTER para continuar")
 


    