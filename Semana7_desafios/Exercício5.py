from time import sleep

min = int(input('Qual o minuto inicial? '))
if min == 0:
    segundos = int(input('Quantos segundos então? '))
    for s in range(segundos, -1, -1):
        minutos = s // 60  
        segundos_restantes = s % 60 
        if s <= 10: 
            print(f'\033[1;31m{minutos:02}:{segundos_restantes:02}\033[0m')
        else:
            print(f'{minutos:02}:{segundos_restantes:02}')
        sleep(1.0)
else:
    for i in range(min, -1, -1):
        for j in range(59, -1, -1):
            if i <= 10 and j <= 10:
                print(f'\033[1;31m{i:02}:{j:02}\033[0m')
            else:
                print(f'{i:02}:{j:02}')
            sleep(1.0)
    
print('FIM') 