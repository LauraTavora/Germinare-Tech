# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

temp = float(input('Informe a temperatura em °C: '))
f = ((9 * temp) / 5) + 32

print(f'A temperatura de {temp}°C corresponde a {f}°F!')