linhas = int(input('Qual o tamanho do triângulo? '))
for i in range(0, linhas):
    for j in range(i, linhas):
        print('*', end= ' ')
    print()