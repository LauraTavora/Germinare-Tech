import random

def jogo_de_adivinhacao(nivel):
    if nivel == "FACIL":
        numero_aleatorio = random.randint(1, 10)
        max_tentativas = 5
    elif nivel == "MEDIO":
        numero_aleatorio = random.randint(1, 50)
        max_tentativas = 7
    elif nivel == "DIFICIL":
        numero_aleatorio = random.randint(1, 100)
        max_tentativas = 10
    else:
        print("Nível inválido. Escolha entre FACIL, MEDIO ou DIFICIL.")
        return

    tentativas = 0

    while True:
        tentativa = int(input(f"Tente adivinhar o número (entre 1 e {numero_aleatorio}): "))
        tentativas += 1

        if tentativa == numero_aleatorio:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
            break
        elif tentativa < numero_aleatorio:
            print("Tente novamente. O número é maior.")
        else:
            print("Tente novamente. O número é menor.")

        if tentativas >= max_tentativas:
            print(f"Você atingiu o número máximo de tentativas ({max_tentativas}). O número correto era {numero_aleatorio}.")
            break

if __name__ == "__main__":
    print("Bem-vindo ao Jogo de Adivinhação!")
    
    while True:
        nivel = input("Escolha o nível (FACIL, MEDIO ou DIFICIL): ").upper()
        if nivel in ["FACIL", "MEDIO", "DIFICIL"]:
            break
        else:
            print("Nível inválido. Por favor, escolha entre FACIL, MEDIO ou DIFICIL.")
    
    jogo_de_adivinhacao(nivel)
