import keyboard


def notas():
    alunos = int(input('Quantos alunos a turma tem? '))

    media = 0
    maior = 0
    menor = 0 
    aprovados = 0 
    reprovados = 0
    maior_media = ''
    menor_media = ''
    quantidade_alunos = 1


    while(quantidade_alunos <= alunos):
        nome = input(f'Nome do {quantidade_alunos + 0}º aluno: ')
        nota1 = float(input(f'Digite a primeira nota de {nome}: '))
        nota2 = float(input(f'Digite a segunda nota de {nome}: '))
        nota3 = float(input(f'Digite a terceira nota de {nome}: '))
        media = (nota1 * 0.20) + (nota2 * 0.30) + (nota3 * 0.50)
        print(f'Média final de {nome} = {media:.1f}, deseja passar para o próximo aluno?')

        while True:
            proximo = input('S/N:')
            if (proximo.lower() in ('n','nn','nao','não')):
                    print(f'Digite enter para colocar as notas de {nome} novamente')
                    if keyboard.read_key('enter'):
                        nota1 = float(input(f'Digite a primeira nota de {nome}: '))
                        nota2 = float(input(f'Digite a segunda nota de {nome}: '))
                        nota3 = float(input(f'Digite a terceira nota de {nome}: '))
                        media = (nota1 * 0.20) + (nota2 * 0.30) + (nota3 * 0.50)
                        print(f'Média final de {nome} = {media:.1f}, deseja passar para o próximo aluno?')    
            else: 
                 break  
        quantidade_alunos += 1 

        if media >= 7:
                aprovados += 1
        else:
                reprovados += 1
        
        total_aprovados = (aprovados / alunos) * 100
        total_reprovados = (reprovados / alunos) * 100


        if media > maior:
            maior = media
            maior_media = nome
        if menor == 0 or media < menor:
            menor = media
            menor_media = nome
        else:
            media = 0 
            
        
            
        
    print('A turma teve:')
    print(f'- Aprovados: {aprovados} - {total_aprovados:.2f}%')
    print(f'- Reprovados: {reprovados} - {total_reprovados:.2f}%')
    print(f'Maior média: {maior} do aluno {maior_media}')
    print(f'Menor média: {menor} do aluno {menor_media}')
        
notas()
