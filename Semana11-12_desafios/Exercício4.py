while True:
    A = float(input('Digite o valor do lado A: '))
    B = float(input('Digite o valor do lado B: '))
    C = float(input('Digite o valor do lado C: '))

    if A <= 0 or B <= 0 or C <= 0 or A >= (B + C) or B >= (A + C) or C >= (A + B):
        print('Valores inválidos!')
    else:
        if A == B and A == C:
            print('O triângulo que esses lados formam é o triângulo Equilátero!')
        elif A == B or A == C or B == C:
            print('O triângulo que esses lados formam é o triângulo Isósceles!')
        else:
            print('O triângulo que esses lados formam é o triângulo escaleno')
