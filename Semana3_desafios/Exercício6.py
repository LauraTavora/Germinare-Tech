horas = int(input('Qual a hora de agora?'))
min = int(input('Quais os minutos agora?'))

def minutos_passados(horas,min):
    num1 = (horas * 60) + min
    return num1 

def minutos_faltantes():
    #O total de minutos de um dia é de 1440
    minutos_dia = 1440
    return minutos_dia - ((horas * 60) + min) 

print(f'Já se passaram {minutos_passados(horas,min)} minutos desde o inicio do dia')
print(f'Ainda faltam {minutos_faltantes()} para encerrar o dia de hoje')