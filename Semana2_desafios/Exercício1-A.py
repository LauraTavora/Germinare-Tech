seg = int(input('Digite um horário em segundos:'))

horas = seg // 3600
resto = seg % 3600
minutos = resto // 60 
segundos = resto % 60 

print (horas,'h',minutos,'min',segundos,'s')