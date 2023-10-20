def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print('---' * 3)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    diagonal1 = [tabuleiro[i][i] for i in range(3)]
    diagonal2 = [tabuleiro[i][2 - i] for i in range(3)]

    if all(celula == jogador for celula in diagonal1) or all(celula == jogador for celula in diagonal2):
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    rodada = 1

    while True:
        print("Rodada", rodada)
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Linha: ")) - 1
        coluna = int(input("Coluna: ") - 1)

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2 or tabuleiro[linha][coluna] != " ":
            print("Opção inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            print("Jogador", jogador, "ganhou após", rodada, "rodadas")
            break

        if " " not in [celula for linha in tabuleiro for celula in linha]:
            print("O jogo terminou em empate.")
            break

        jogador = "O" if jogador == "X" else "X"
        rodada += 1

jogar_jogo_da_velha()
