dados = list()
dados.append('Pedro')
dados.append(25)

dados2 = list()
dados2.append('Maria')
dados2.append(19)

dados3 = list()
dados3.append('João')
dados3.append(32)

pessoas = []
pessoas.append(dados[:]) #Adicionei a pessoas uma cópia de dados
pessoas.append(dados2[:])
pessoas.append(dados3[:])

print(pessoas[0][0]) #O resultado vai ser "Pedro"
print(pessoas[1][1]) #O resultado vai ser "19"
print(pessoas[2][0]) #O resultado vai ser "João"
print(pessoas[1]) #O resultado vai mostrar a cópia de "dados2"