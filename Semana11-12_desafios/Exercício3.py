while True:
    
    num = int(input('Digite um número para ver a sua tabuada: '))

    print('-=' *20)
    for contador in range(1, 11):
        print(f'{num} x {contador} = {num * contador}')
    print('-=' *20)
    escolha = str(input('Deseja ver outra tabuada? (S/N): ')).upper()
    if escolha == 'S':
        print()
    else:
        break

