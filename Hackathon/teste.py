# Dicionário de perfis de investidor e ativos recomendados
perfis_investidor = {
    "conservador": ["Títulos do Tesouro", "Poupança"],
    "moderado": ["Fundos de Investimento", "Ações Blue Chip"],
    "agressivo": ["Ações de Tecnologia", "Criptomoedas"]
}

# Função para coletar informações do cliente
def coletar_informacoes_cliente():
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    perfil = input("Escolha seu perfil de investidor (conservador, moderado, agressivo): ")
    return nome, data_nascimento, perfil

# Função para recomendar ativos com base no perfil de investidor
def recomendar_ativos(perfil):
    if perfil in perfis_investidor:
        return perfis_investidor[perfil]
    else:
        return ["Perfil de investidor não reconhecido"]

# Função principal
def main():
    nome, data_nascimento, perfil = coletar_informacoes_cliente()
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Perfil de Investidor: {perfil}")
    
    ativos_recomendados = recomendar_ativos(perfil)
    
    if ativos_recomendados:
        print("Ativos recomendados para o seu perfil de investidor:")
        for ativo in ativos_recomendados:
            print(ativo)
    else:
        print("Erro na recomendação de ativos.")

if __name__ == "__main":
    main()
