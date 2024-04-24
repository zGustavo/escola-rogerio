# Inicialização das variáveis de contagem
total_respostas = 0
saboroso = 0
normal = 0
ruim = 0

# Loop para coletar respostas dos usuários
while True:
    # Apresenta as opções para o usuário
    print("Escolha o sabor do chocolate:")
    print("1 - Saboroso")
    print("2 - Sabor Normal")
    print("3 - Gosto Ruim")
    
    # Solicitação da escolha do usuário
    resposta = input("Digite o número correspondente à sua escolha (1, 2 ou 3): ")
    
    # Verifica se a resposta é válida
    if resposta == '1':
        saboroso += 1
        total_respostas += 1
    elif resposta == '2':
        normal += 1
        total_respostas += 1
    elif resposta == '3':
        ruim += 1
        total_respostas += 1
    else:
        # Se a resposta não é válida, encerra o loop
        print("Resposta inválida. Encerrando a pesquisa...")
        break

# Apresenta os resultados finais
print("\nTotal de respostas coletadas:", total_respostas)

if total_respostas > 0:
    # Calcula e apresenta as porcentagens
    percentual_saboroso = (saboroso / total_respostas) * 100
    percentual_normal = (normal / total_respostas) * 100
    percentual_ruim = (ruim / total_respostas) * 100
    
    print("Porcentagem de Saboroso: {:.2f}%".format(percentual_saboroso))
    print("Porcentagem de Sabor Normal: {:.2f}%".format(percentual_normal))
    print("Porcentagem de Gosto Ruim: {:.2f}%".format(percentual_ruim))
