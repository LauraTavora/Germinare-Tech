valores = []
while True:
    valores.append(int(input('Digite um valor qualquer: ')))
    opcao = str(input('Deseja continuar?\n[s = Sim| n = Não]')).lower()
    if (opcao == 'n'):
        break

print('Você digitou',len(valores),'números na lista')
print('A lista ficou assim:')
print(valores)
valores.sort()
print('A lista ordenada ficou assim:')
print(valores)
valores.reverse()
print('A lsita ordenada de forma decrescente ficou assim:')
print(valores)
if 5 in valores:
    print('Você digitou o número 5')
else:
    print('Você não digitou o número 5')