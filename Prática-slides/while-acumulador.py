contador = 1
acumulador = 0
#Programa só para quando o usuário digitar cinco valores diferentes
while (contador <= 5): 
    x = int(input('Digite um valor: '))
    #Vai acumulando os valores digitados, para depois soma-los
    acumulador = acumulador + x 
    contador += 1

print('Acumulador = ', acumulador)