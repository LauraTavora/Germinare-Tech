# Integrantes: Pedro Henrique Alves Martins, Laura Francisco, Matheus Hideki, Daniel Liberato , Kaique Moreira

################################################ CADASTRO DE USUÁRIOS #################################################

import random
listaalunos = []
lista = []

while True:
    nome = input("Digite o nome: ")
    if len(nome) < 3:
        print("Nome inválido")
        continue
    sobrenome = input("Digite o sobrenome: ")
    if len(sobrenome) < 3:
        print("Sobrenome inválido")
        continue
    codigo = random.randint(1000,9999)
    listaalunos.append((nome, sobrenome, codigo))
    print(f"Código: {codigo} - Nome: {nome}")
    continuar = input("Continuar o cadastro? S/N: ").upper()
    if continuar.find("N") == 0:
        break

########################################################################################################################


############################################### REMOÇÃO DE USUÁRIOS ####################################################

remover = input("Deseja remover algum aluno? S/N ").upper()
while True:
        if remover == ("S"):
            codigoremover = int(input("Digite o Código do aluno que o usuário deseja remover: "))
            for alunos in listaalunos:
                for rcodigo in alunos:
                    if rcodigo == codigoremover:
                        listaalunos.remove(alunos)
        elif remover == ("N"):
            break

        cremovendo = input("Deseja continuar removendo? S/N: ")
        if cremovendo.find("N") == 0:
            break

        print(listaalunos)

##########################################################################################################################


################################################ BUSCAR USUÁRIOS #########################################################

buscar = input("Deseja buscar algum aluno? S/N: ").upper()

while True:
    if buscar == ("S"):
        encontrar = int(input("Digite o código do aluno que deseja encontrar: "))
        for alunos in listaalunos:
            if alunos[2] == encontrar:
                print(alunos)
            continuar = input("Deseja continuar? S/N: ").upper()
            if continuar == ("S"):
                continue

###########################################################################################################################


################################################ REGISTROS TOTAIS #########################################################

    print()         
    print(f'Número de Registros: {len(listaalunos)}')
    print()

###########################################################################################################################
    
    
##################################################### MENU ################################################################

    while True:
        print(''' ------------------------ Menu ---------------------------
                Opção 1: Mostrar os usuários por ordem de cadastro   
                Opção 2: Mostrar os usuários em ordem alfabética
                Opção 3: Mostrar os usuários em ordem de código
                        : '''
                        )
        
        escolhamenu = int(input("Digite o número da opção desejada: "))
        if escolhamenu == 1:
                for alunos in listaalunos:
                    print(alunos)
        if escolhamenu == 2:
            for i, alunos in enumerate(listaalunos):
                lista.append(alunos[0])

                lista.sort()
                print(lista)
        
            print(listaalunos)
        if escolhamenu == 3:
                for alunos in listaalunos:
                    print(f'Código: {alunos[2]} Nome: {alunos[0]}')

############################################################################################################################