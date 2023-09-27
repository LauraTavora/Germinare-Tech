de0_25 = 0
de26_50 = 0 
de51_75 = 0
de76_100 = 0

while True:
    contagem = int(input('Digite um número: '))
    if contagem < 0:
        break 
    if contagem > 100:
        break

    if contagem >= 0 and contagem <= 25:
        de0_25 += 1
    elif contagem >= 26 and contagem <= 50:
        de26_50 += 1
    elif contagem >= 51 and contagem <= 75:
        de51_75 += 1
    elif contagem >= 76 and contagem <= 100:
        de76_100 += 1
    else:
        de0_25 += 0
        de26_50 += 0
        de51_75 += 0
        de76_100 += 0 

print(f'A quantidade de números entre 0 e 25 foi igual a {de0_25}')
print(f'A quantidade de números entre 26 e 50 foi igual a {de26_50}')
print(f'A quantidade de números entre 51 e 75 foi igual a {de51_75}')
print(f'A quantidade de números entre 76 e 100 foi igual a {de76_100}')