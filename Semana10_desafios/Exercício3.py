palavra = str(input('Digite uma palavra qualquer: '))

def contar_letras(palavra):
    letras = {}

    for alfabeto in palavra:

        if alfabeto in letras:
           letras[alfabeto] += 1
        else:
           letras[alfabeto] = 1

    for alfabeto, vezes in letras.items():
        print(f'Letra {alfabeto} aparece {vezes} vezes')

contar_letras(palavra)