def definaCedulas(montante):
    notas100 = montante // 100
    montante %= 100
    if notas100 != 0:
        print(f"Cédulas de R$100,00 = {notas100}")

    notas50 = montante // 50
    montante %= 50
    if notas50 != 0:
        print(f"Cédulas de R$50,00 = {notas50}")

    notas10 = montante // 10
    montante %= 10
    if notas10 != 0:
        print(f"Cédulas de R$10,00 = {notas10}")

    notas5 = montante // 5
    montante %= 5
    if notas5 != 0:
        print(f"Cédulas de R$5,00 = {notas5}")

    notas2 = montante // 2
    montante %= 2
    if notas2 != 0:
        print(f"Cédulas de R$2,00 = {notas2}")


saque = int(input("Digite o valor do saque: "))
print('=' *30)
print('====== CAIXA ELETRÔNICO ======')
print('=' *30)
if 10 <= saque <= 600:
    definaCedulas(saque)
else:
    print("Valor de saque fora do intervalo permitido. O valor mínimo é 10 reais e o máximo é 600 reais.")
