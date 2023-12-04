salario = int(input('Qual o seu salário? '))

def imposto_renda(salario):
    if salario <= 1000:
        print('Você não precisa pagar o imposto de renda!')
    if salario >= 1001 and salario <= 3000:
        imposto = salario / 10
        print(f'O imposto de renda a ser pago é R${imposto:.2f}')
    if salario >= 3001 and salario <= 5000:
        imposto2 = salario / 20 
        print(f'O imposto de renda a ser pago é R${imposto2:.2f}')
    if salario > 5000:
        imposto3 = salario / 30
        print(f'O imposto de renda a ser pago é R${imposto3:.2f}')



imposto_renda(salario)