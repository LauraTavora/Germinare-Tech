germinare_business = int(input('Quantos alunos tem hoje dentro da escola Germinare Business? '))
germinare_tech = int(input('Quantos alunos tem hoje dentro da escola Germinare TECH? '))

if germinare_tech > germinare_business:
    print('A Germinare TECH já ultrapassou a Germinare Business')
else:
    anos = 0
    while germinare_tech * (1 + 0.50)** anos <= germinare_business * (1 + 0.10)** anos:
        anos += 1

print(f'A Germinare TECH ultrapassará a Germinare Business em aproximadamente {anos} anos')