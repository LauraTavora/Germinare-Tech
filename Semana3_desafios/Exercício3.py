nome = input('Digite seu nome completo:')
email = input('Digite seu e-mail:')


def validar_email_usuario(email):
     valindando_email = "@" in email.lower() and ".com.br" in email.lower()
     return valindando_email


print (f'E-mail do usuário {nome} é valido? {validar_email_usuario(email)}')