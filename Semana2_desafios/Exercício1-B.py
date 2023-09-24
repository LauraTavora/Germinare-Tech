entrada_usuario = input('Digite um horário no formato "hora:minuto:segundo": ')
partes = entrada_usuario.split(":")

hora = int(partes[0])
minuto = int(partes[1])
segundo = int(partes[2])

total_segundos = hora * 3600 + minuto * 60 + segundo


print(f"O horário {entrada_usuario} equivale a {total_segundos} segundos.")