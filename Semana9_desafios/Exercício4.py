import math


modelos = []
quilometros = []


print('Comparativo de Consumo de Combustível')
print()
print()

for i in range(1, 6):
    print(f'Veiculo {i}')
    modelo = str(input('Modelo: '))
    quilometro = float(input('Km por litro: ')) 
    print('=' * 20)
    modelos.append(modelo)
    quilometros.append(quilometro)

litros = []
gastos= []
 
for i in range(5):
    litro = math.ceil(1000 / quilometros[i])
    valor = litro * 2.25
    litros.append(litro)
    gastos.append(valor)
    carro_economico = quilometros.index(max(quilometros))

print()
print()
print('Relátorio Final')
for i in range(5):
    print(f'{i + 1} - {modelos[i]} - {quilometros[i]:.1f} - {litros[i]:.2f} litros - R${gastos[i]:.2f}')

economico = modelos[carro_economico]
print(f'O menor consumo é do {economico}')
