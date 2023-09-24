def cobrando_tarifas():
    tempo_entrada = (horario_entrada * 60) + min_entrada 
    tempo_saida = (horario_saida * 60) + min_saida
    tempo_estacionado = tempo_saida - tempo_entrada

    horas_estacionadas = (tempo_estacionado + 59) // 60

   
    preco = 0

    if horas_estacionadas <= 2:
        preco = horas_estacionadas * 1.00 
    elif horas_estacionadas <= 4:
        preco = horas_estacionadas * 1.00 + 0.40 
    else:
        preco = horas_estacionadas * 1.80
    return preco

horario_entrada = int(input('Qual a hora de entrada?'))
min_entrada = int(input('Qual o minuto de entrada?'))
horario_saida = int(input('Qual a hora da saida?'))
min_saida = int(input('Qual o minuto de saida?'))

print(f'A JBS cobra pelo seu estacionamento: R${cobrando_tarifas():.2f}')
