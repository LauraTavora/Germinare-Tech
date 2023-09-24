def eh_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def eh_armstrong(numero):
    num_str = str(numero)
    n = len(num_str)
    soma = sum(int(digit) ** n for digit in num_str)
    return soma == numero

def eh_quadrado_perfeito(numero):
    raiz = int(numero ** 0.5)
    return raiz * raiz == numero

def eh_palindromo(numero):
    num_str = str(numero)
    return num_str == num_str[::-1]

def tem_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

while True:
    
        numero = int(input("Digite um número inteiro positivo (ou 0 para sair): "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
        elif numero == 0:
            break
        else:
            print(f"O número {numero} é {eh_par_impar(numero)}")
            print(f"O número {numero} {'é' if eh_primo(numero) else 'não é'} primo")
            print(f"O número {numero} {'é' if eh_armstrong(numero) else 'não é'} um número de Armstrong")
            print(f"O número {numero} {'é' if eh_quadrado_perfeito(numero) else 'não é'} um quadrado perfeito")
            print(f"O número {numero} {'é' if eh_palindromo(numero) else 'não é'} um palíndromo")
            print(f"O número {numero} {'está na' if tem_fibonacci(numero) else 'não está na'} sequência de Fibonacci")
    

