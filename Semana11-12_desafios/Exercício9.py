num = int(input('Digite um número entre 1 e 50: '))
while True:
    if num < 0 or num > 50:
        print('ERRO: o número deve estar entre 1 e 50!')
        num = int(input('Digite um número entre 1 e 50: '))
        for i in range(0, num):
            print(' '*i, (i+1))
