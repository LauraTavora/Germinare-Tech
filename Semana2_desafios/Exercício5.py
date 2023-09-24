tamanho_arquivo = int(input('Digite o tamanho do arquivo em MB:'))
velocidade_conexao = int(input ('Digite a velocidade da conexão em Mbps:'))

arquivo_megabits = tamanho_arquivo * 8
tempo_estimado = (arquivo_megabits/velocidade_conexao)
velocidade_dowload = tempo_estimado <= 60

print (f'O tempo estimado de dowload é de {tempo_estimado:.2f} segundos')
print ('Dowload rápido?', velocidade_dowload)