def validar_entrada():
    while True:
        numero = str(input('Digite um número inteiro positivo de 10 dígitos: '))
        if len(numero) == 10 and numero.isdigit():
            soma = 0
            for digito in numero:
                soma += int(digito)
            media = soma / 10
            if media is not None:
                print(f'Número lido = {numero}')
                print(f'Média = ({numero}) / 10 = {soma}/10 = {media:.1f}')
                print(f'Dígito verificador = {int(media)}')
                break
            else:
                print('Número não é válido. Tente novamente.')
        else:
            print('Entrada inválida. Certifique-se de que você digitou um número inteiro positivo de 10 dígitos')

validar_entrada()
