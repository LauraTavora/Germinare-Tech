linhas = int(input('Qual o tamanho do triângulo? '))


div = linhas // 2

for i in range(0, div):

    for j in range(i, linhas):
        print(' ', end= ' ')

    for k in range(0, 2 * i + 1):
        print('*', end=' ')

    print()