def quantas (valor,cedula):
    if (valor >= cedula):
        if ((valor % cedula != 1) and (valor % cedula != 3)):
            return valor // cedula
        else:
            if (valor // cedula > 1):
                nValor = valor // cedula - 1
                return nValor
            else:
                return 0
    else:
        return 0
    
def defineCedulas(montante):
    n200 = quantas(montante, 200)
    nMon = montante - (n200 * 200)
    if not(nMon == 0 and n200 == 0):
        if n200 != 0:
            print('Cédulas R$200,00 = ', n200) 
        montante = nMon
    n100 = quantas(montante, 100)
    nMon = montante - (n100 * 100)
    if not(nMon == 0 and n100 == 0):
        if n200 != 0:
            print('Cédulas R$100,00 = ', n100) 
        montante = nMon
    n50 = quantas(montante, 50)
    nMon = montante - (n50 * 50)
    if not(nMon == 0 and n50 == 0):
        if n50 != 0:
            print('Cédulas R$50,00 = ', n50) 
        montante = nMon
    n20 = quantas(montante, 20)
    nMon = montante - (n20 * 20)
    if not(nMon == 0 and n20 == 0):
        if n20 != 0:
            print('Cédulas R$20,00 = ', n20) 
        montante = nMon
    n10 = quantas(montante, 10)
    nMon = montante - (n10 * 10)
    if not(nMon == 0 and n10 == 0):
        if n10 != 0:
            print('Cédulas R$10,00 = ', n10) 
        montante = nMon
    n5 = quantas(montante, 5)
    nMon = montante - (n5 * 5)
    if not(nMon == 0 and n5 == 0):
        if n200 != 0:
            print('Cédulas R$5,00 = ', n5) 
        montante = nMon
    n2 = quantas(montante, 2)
    nMon = montante - (n2 * 2)
    if not(nMon == 0 and n2 == 0):
        if n200 != 0:
            print('Cédulas R$2,00 = ', n2) 
        montante = nMon


retirado = int(input('Qual será o valor para saque? '))
print('=' *30)
print('====== CAIXA ELETRÔNICO ======')
print('=' *30)
if 5 <= retirado <= 5000:
    defineCedulas(retirado)
else:
    print('Valor Inválido. O valor para saque deve estar entre R$5,00 e R$5000,00')


    