import math

num = int(input('Digite um número: '))
numero = num
bina = list()


while num > 0:
    if num % 2 == 1:
        bina.append(1)
        num = math.floor(num / 2)
    if num % 2 == 0:
        bina.append(0)
        num = math.floor(num / 2)

bina.reverse()
print(f'O número {numero}, em decimal é: ', end='')
for i in range(1, len(bina)):
    print(bina[i], end='')