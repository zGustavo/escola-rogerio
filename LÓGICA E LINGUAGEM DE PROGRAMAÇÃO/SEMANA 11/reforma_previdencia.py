# Perguntando o sexo do usuário
sexo = input("Qual seu sexo (M/F)? ").strip().upper()

# Perguntando a idade em que o usuário começou a contribuir
idade_inicio_contribuicao = int(input("Com que idade começou a contribuir? ").strip())

# Definindo as idades mínimas para aposentadoria e o tempo de contribuição necessário
if sexo == 'M':
    idade_minima_aposentadoria = 65
elif sexo == 'F':
    idade_minima_aposentadoria = 62
else:
    print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
    exit()

# Calculando o tempo de contribuição até a idade mínima de aposentadoria
tempo_contribuicao_minimo = idade_minima_aposentadoria - idade_inicio_contribuicao

# Verificando se o usuário atingirá a idade mínima com o tempo mínimo de contribuição
if tempo_contribuicao_minimo < 25:
    print(f"Você precisará contribuir até os {idade_inicio_contribuicao + 25} anos para cumprir o tempo mínimo de contribuição de 25 anos.")
    print(f"Com essa idade você terá direito a 60% do benefício.")
    print(f"Para receber 100% do benefício, você precisará contribuir até os {idade_inicio_contribuicao + 40} anos.")
else:
    # O usuário atingirá a idade mínima e tempo de contribuição mínima ao mesmo tempo ou antes
    if tempo_contribuicao_minimo == 25:
        porcentagem_beneficio = 60  # 60% é o benefício mínimo após 25 anos de contribuição
    else:
        # Cálculo do benefício baseado no tempo de contribuição (após o mínimo de 25 anos)
        anos_extra = tempo_contribuicao_minimo - 25
        porcentagem_beneficio = 60 + anos_extra * 2.5
        if porcentagem_beneficio > 100:
            porcentagem_beneficio = 100

    print(f"Você só terá direito a se aposentar com {idade_minima_aposentadoria} anos.")
    print(f"Com essa idade você terá direito a {porcentagem_beneficio}% do benefício.")

    # Calculando a idade para receber 100% do benefício
    idade_100_beneficio = idade_inicio_contribuicao + 40

    # Se a idade para 100% for menor que a idade mínima de aposentadoria, ajustamos para a idade mínima
    if idade_100_beneficio < idade_minima_aposentadoria:
        idade_100_beneficio = idade_minima_aposentadoria

    print(f"Para receber 100% do benefício, você precisará trabalhar até os {idade_100_beneficio} anos.")
