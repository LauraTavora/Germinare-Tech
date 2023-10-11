valor = int(input('Digite um valor qualquer: '))

Tupla1 = (5,10,6,7,5)

def repetidos(tupla, numero):
    quantidade = tupla.count(numero)

    if quantidade > 1:
        print(f'Na Tupla1 o número {valor} aparece {quantidade} vezes ')
    else:
        print(f'O número {valor} não aparece na lista')


    return quantidade

repetidos(Tupla1, valor)