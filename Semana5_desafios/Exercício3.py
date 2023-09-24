while True:
    numero = int(input("Digite um número inteiro positivo (ou um número negativo para encerrar): "))
    
    if numero < 0:
        break  # Encerra o programa se o número for negativo
    
    soma_impares = 0
    contador_impares = 0
    
    for i in range(1, numero + 1):
        if i % 2 != 0:
            contador_impares += 1

    soma_impares += numero

    
    print(f"A quantidade de números ímpares entre 1 e {numero} é: {contador_impares}")
    print(f'A soma dos números impares entre 1 e {numero} é: {soma_impares}')
