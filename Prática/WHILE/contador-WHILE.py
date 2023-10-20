contador = 1
while (contador <= 5): #Enquanto o contador for menor que '5' o código se repete
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    media = (nota1+nota2+nota3)/3
    print(f'A média do aluno é de: {media:.1f}')
    if (media >= 6):
        print('Aluno Aprovado!')
    else:
        print('Aluno Reprovado!')
    contador = contador + 1
    #Acrescenta '1' a cada vez que o código for concluido, até chegar em '5'