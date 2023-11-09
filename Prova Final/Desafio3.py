veiculos = {}

def estacionamento():
    while True:
        placa = input('Qual a sua placa para registrarmos? ')
        pergunta = input('Entrada ou Saída? ').upper()

        if pergunta == 'ENTRADA':
            horario_entrada = int(input('Qual a hora de entrada? '))
            min_entrada = int(input('Qual o minuto de entrada? '))
            tempo_entrada = (horario_entrada * 60) + min_entrada

            veiculos[placa] = {'entrada': tempo_entrada, 'saida': None}

            continuar = input('Deseja colocar o horário de saída desse veículo? ').upper()
            if continuar == 'S':
                while True:
                    verificacao = input('Digite a placa para verificação: ')
                    if verificacao in veiculos and veiculos[verificacao]['saida'] is None:
                        horario_saida = int(input('Qual a hora de saída? '))
                        min_saida = int(input('Qual o minuto de saída? '))
                        tempo_saida = (horario_saida * 60) + min_saida
                        veiculos[verificacao]['saida'] = tempo_saida
                        calcular_tempo_total(verificacao)
                        break
                    elif verificacao not in veiculos:
                        print(f'A placa "{verificacao}" não existe no sistema. Digite outra placa.')

        elif pergunta == 'SAIDA':
            while True:
                verificacao = input('Digite a placa para verificação: ')
                if verificacao in veiculos and veiculos[verificacao]['saida'] is None:
                    horario_saida = int(input('Qual a hora de saída? '))
                    min_saida = int(input('Qual o minuto de saída? '))
                    tempo_saida = (horario_saida * 60) + min_saida
                    veiculos[verificacao]['saida'] = tempo_saida
                    calcular_tempo_total(verificacao)
                elif verificacao not in veiculos:
                    print(f'A placa "{verificacao}" não existe no sistema. Digite outra placa.')

def calcular_tempo_total(placa):
    tempo_entrada = veiculos[placa]['entrada']
    tempo_saida = veiculos[placa]['saida']
    tempo_total = (tempo_saida - tempo_entrada) / 60
    if tempo_total < 10:
        print(f'O veículo com placa "{placa}" permaneceu no estacionamento por 0{tempo_total} horas.')
    else:
        print(f'O veículo com placa "{placa}" permaneceu no estacionamento por {tempo_total} horas.')


estacionamento()