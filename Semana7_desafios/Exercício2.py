de0_2 = 0
de3_10 = 0
de11_14 = 0
de15_18 = 0
de19_21 = 0
de22_60 = 0
de60_100 = 0
todas_idades = 0
maior = 0
menor = 0

for i in range(0,80):
    idade = int(input('Digite a sua idade: '))
    todas_idades += idade
    media = todas_idades/80


    if idade > maior:
        maior = idade
    if menor == 0 or idade < menor:
        menor = idade
    else:
        idade = 0 
    
    if idade < 0:
        print('Idade Inválida!')
        break
    else:
        if idade >= 0 and idade <= 2:
            de0_2 += 1
        elif idade >= 3 and idade <= 10:
            de3_10 += 1
        elif idade >= 11 and idade <= 14:
            de11_14 += 1
        elif idade >= 15 and idade <= 18:
            de15_18 += 1
        elif idade >= 19 and idade <= 21:
            de19_21 += 1
        elif idade >= 22 and idade <= 60:
            de22_60 += 1
        elif idade >= 61 and idade <= 100:
            de60_100 += 1
        else:
            de0_2 += 0
            de3_10 += 0
            de11_14 += 0
            de15_18 += 0 
            de19_21 += 0
            de22_60 += 0
            de60_100 += 0


print(f'A média das idades é {media:.1f} anos')

print(f'A pessoa mais nova tem {menor} anos')
print(f'A pessoa mais velha tem {maior} anos')

print(f'Bebês: {de0_2}')
print(f'Crianças: {de3_10}')
print(f'Pré-adolescente: {de11_14}')
print(f'Adolescente: {de15_18}')
print(f'Jovem: {de19_21}')
print(f'Adulto: {de22_60}')
print(f'Idoso: {de60_100}')