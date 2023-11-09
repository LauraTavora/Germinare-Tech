numeros_escritos = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')


while True:
    num = int(input('Digite um número: '))
    if 1 <= num <= 10:
        numeros = numeros_escritos[num - 1]
        print(f'Você digitou o número {numeros}')
    else:
        print('FIM!!!')
        break