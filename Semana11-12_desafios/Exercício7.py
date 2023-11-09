def ano_bissexto():
    ano = int(input('Qual o ano que você deseja analisar? '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é Bissexto!')
    else:
        print(f'O ano {ano} não é Bissexto!')
    return ano

#ano_bissexto()

def verificando_data():
    print('==================== Analisando uma data ====================')
    dia = int( input('Dia: ') )
    mes = int( input('Mês: ') )
    ano = int( input('Ano: ') )


    meses_31 = (1, 3, 5, 7, 8, 10, 12)
    meses_30 = (4, 6, 9, 11)
    

    if mes in meses_31:
        if dia >= 1 and dia <= 31:
            print('Data válida')
        else:
            print('Data inválida')
    if mes in meses_30:
        if dia >= 1 and dia <= 30:
            print('Data válida')
        else:
            print('Data inválida')
    if mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia >= 1 and dia <= 29:
                print('Data válida')
            else:
                print('Data inválida')
        elif dia >= 1 and dia <= 28:
                print('Data inválida')


verificando_data()