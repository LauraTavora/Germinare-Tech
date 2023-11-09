inicio = int(input('Digite um número para ser o inicio: '))
fim = int(input('Digite um número para ser o fim: '))

if fim <= inicio:
    print('O valor de "fim" deve ser maior que o valor de "inicio". Vou inverter os valores')
    inicio, fim = fim, inicio

print(f'Valores divisiveis por 5 no intervalo de {inicio} e {fim} são: ')
for i in range(inicio, fim + 1):
    if i % 5 == 0:
        print(i)
