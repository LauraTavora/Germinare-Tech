assinantes = (10000,10500,11000,11200,11500,11800)
novos_clientes = (0,500,1000,1200,1500,1800)
cancelamentos = (500,450,500,200,300,200)
acessos_canal_rural = (2000,2200,2500,2600,2700,2800)

retencao_maxima_total = 0
retencao_maxima_rural = 0

meses_totais = 0
meses_rurais = 0


for i in range(1, len(assinantes)):
    retencao_total = (1 - (assinantes[i] - novos_clientes[i]) / assinantes[i])* 100

    if retencao_total > retencao_maxima_total:
        retencao_maxima_total = retencao_total
        meses_totais = i + 1
    elif retencao_total == retencao_maxima_total:
        meses_totais.append(i + 1)

   
    print(f'A taxa de retenção para os assinantes totais no mês {i + 1} é de: {retencao_total:.2f}')


print()
print()

for i in range(1, len(assinantes)):
    retencao_rural = (1 - (assinantes[i] - acessos_canal_rural[i]) / assinantes[i]) * 100


    if retencao_rural > retencao_maxima_rural:
        retencao_maxima_rural = retencao_rural
        meses_rurais = i + 1
    elif retencao_rural == retencao_maxima_rural:
        meses_rurais.append(i +1)

    print(f'A taxa de retenção para os assinantes que acessam o Canal Rural no mês {i + 1} é de: {retencao_rural:.2f} ')



print(f'Meses com a maior retenção com os assinantes totais:{meses_totais}')
print(f'A maior taxa de retenção com os assinantes no total foi de {retencao_maxima_total:.2f}')

print()

print(f'Meses com a maior retenção com os assinantes que acessam o Cana Rural é de:{meses_rurais}')
print(f'A maior taxa de retenção com os assinantes que acessam o Canal Rural foi de {retencao_maxima_rural:.2f}')

    
