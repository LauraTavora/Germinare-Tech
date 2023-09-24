nome = input('Digite seu nome completo:')
email = input('Digite seu e-mail:')


def validar_email_usuario(email):
     valindando_email = "@" in email.lower() and ".com.br" in email.lower()
     return valindando_email


print (f'E-mail do usuário {nome} é valido? {validar_email_usuario(email)}')

print('-----------------------------------------------------------------------')
def validar_senha(senha):
    #maiuscula = False
    #minuscula = False
    #caracter_especial = False
    maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minuscula = 'abcdefghijklmnopqrstuvwxyz'
    caracteres_especiais = ['!', '@', '#', '$', '%']

    if len(senha) < 8:
        return False
    
    if senha in maiuscula:
        if maiuscula.isupper():
            maiuscula = True
        
        elif minuscula.islower():
            minuscula = True
       
        elif senha in caracteres_especiais:
            caracteres_especiais = True

    
    if maiuscula and minuscula and caracteres_especiais:
        return True
    else:
        return False


senha = input("Digite sua senha: ")


if validar_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida.")