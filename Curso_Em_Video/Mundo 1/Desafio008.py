# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite uma distância em metros: '))
print(f'A medida de {medida:.1f} corresponde a:')
km = medida / 1000
print(f'{km}km')

hm = medida / 100
print(f'{hm}hm')

dam = medida / 10
print(f'{dam}dam')

cm = medida * 100
print(f'{cm:.0f}cm')

mm = medida * 100
print(f'{mm:.0f}mm')

# OU
print()
km = medida / 1000
hm = medida / 100
dam = medida / 10
cm = medida * 100
mm = medida * 100
print(f'''A medida de {medida:.1f} corresponde a:
{km}km
{hm}hm
{dam}dam
{cm:.0f}cm
{mm:.0f}mm''')