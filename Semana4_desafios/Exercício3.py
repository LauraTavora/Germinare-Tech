import random, datetime 
from datetime import datetime

def validando_email(chave):
     valindando_email = "@" in chave.lower() and ".com.br" in chave.lower()
     return valindando_email 


nome = input('Nome do cliente? ')
agencia = int(input('Qual agência do cliente? '))
conta_corrente = int(input('Qual o número da conta corrente do cliente? '))
enviar_para = input('Para quem o cliente irá fazer a transferência? ')
instituicao = input('Qual a instituição do cliente? ')

while True:
    chave = input('Qual a chave do cliente? ')
    if validando_email(chave):
        break
    else:
        print('Email inválido. Digite o email com "@" e com ".com.br"')

cpf = input('Qual o cpf do cliente? ')
valor = int(input('Qual o valor para transferência? '))


def data_atual():
    hoje = datetime.now()
    return hoje.date()


def gerando_id():
    return random.randint(10000000,  99999999)


def cpf_formatado(cpf):
    return (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')


def formatar_agencia(agencia):
    formatacao = (f'{agencia:04}')
    return formatacao


def validando_email(chave):
     valindando_email = "@" in chave.lower() and ".com.br" in chave.lower()
     return valindando_email


def cor_saldo(valor):
    class color:
        AZUL = '\033[94m'
        VERDE = '\033[92m'
        AMARELO = '\033[93m'
        VERMELHO = '\033[91m'
        NEGRITO ='\033[1m'
        SUBLIHANDO = '\033[4m'
        NORMAL = '\033[0;0m'
    
    valor_formatado = f'R${valor:.2f}'
    if valor >= 1500:
        return (f'{color.AZUL}Valor: {valor_formatado}{color.NORMAL}')
    else:
        return (f'{color.VERMELHO}Valor: {valor_formatado}{color.NORMAL}')


def exibirExtrato(nome,agencia,conta_corrente,enviar_para,instituicao,chave,cpf,valor):

    print('\033[1;32mDADOS DO CLIENTE\033[0m')
    print(f'Nome: {nome}')
    print(f'Agência: {formatar_agencia(agencia)}')
    print(f'Conta Corrente: {conta_corrente}')

    print('\033[1;34m  ---------------------------------\033[0m')

    print('\033[1;32mDADOS DA TRANSFERÊNCIA\033[0m')
    print(f'Para: {enviar_para}')
    print(f'Instituição: {instituicao}')
    print(f'Chave: {chave}')
    print(f'CPF: {cpf_formatado(cpf)}')
    print(f'{cor_saldo(valor)}')

    print('\033[1;34m  ---------------------------------\033[0m')

    print('\033[1;32mID/Transação\033[0m')
    print(f'ID:{gerando_id()}')
    print(f'Data:{data_atual()}')


exibirExtrato(nome,agencia,conta_corrente,enviar_para,instituicao,chave,cpf,valor)


