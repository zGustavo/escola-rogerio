programa {
  funcao inicio() {
    inteiro total_respostas, saboroso, normal, ruim
    inteiro resposta

    // Inicialização das variáveis de contagem
    total_respostas = 0
    saboroso = 0
    normal = 0
    ruim = 0
    resposta = 0

    // Loop para coletar as respostas dos usuários
    enquanto (resposta >= 0 e resposta <= 3) {
      // Apresenta as opções para o usuário
      escreva("Escola o sabor do chocolate:\n")
      escreva("1 - Saboroso\n")
      escreva("2 - Sabor normal\n")
      escreva("3 - Gosto ruim\n")

      // Solicitação da escolha do usuário
      escreva("Digite o número correspondente à sua escolha (1, 2 ou 3): ")
      leia(resposta)

      // Verifica e processa a resposta do usuário
      escolha(resposta) {
        caso 1:
          saboroso = saboroso + 1
          total_respostas = total_respostas + 1
          pare
        caso 2:
          normal = normal +1
          total_respostas = total_respostas + 1
          pare
        caso 3:
          ruim = ruim +1
          total_respostas = total_respostas + 1
          pare
        caso contrario:
          // Se a resposta não é válida, encerra o loop
          escreva("Encerrando a pesquisa...\n")

      }

    }

    // Apresenta os resultados finais
    escreva("\nTotal de respostas coletadas: ", total_respostas, "\n")

    se (total_respostas > 0) {
      // Calcula e apresenta as porcentagens
      real percentualSaboroso, percentualNormal, percentualRuim
      percentualSaboroso = (saboroso / total_respostas) * 100
      percentualNormal = (normal / total_respostas) * 100
      percentualRuim = (ruim / total_respostas) * 100

      escreva("Porcentagem de Saboroso: ", percentualSaboroso, "%\n")
      escreva("Porcentagem de Sabor Normal: ", percentualNormal, "%\n")
      escreva("Porcentagem de Gosto Ruim: ", percentualRuim, "%\n")
    }
  }
}
