nome = input('Qual o nome do funcionário?\n')
horas = int(input(f'Quantas horas por semana {nome} trabalha?\n'))
dep = int(input(f'Quantos dependentes {nome} tem?\n'))

horas_pagas = 25
valor_pago_dep = 500


salario_mensal = (horas * horas_pagas)*4 + (dep * valor_pago_dep)
print(f'{nome} terá um salário mensal de R${salario_mensal:.2f}')