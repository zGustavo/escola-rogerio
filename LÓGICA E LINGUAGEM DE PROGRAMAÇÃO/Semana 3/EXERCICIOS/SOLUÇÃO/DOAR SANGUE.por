programa {
  funcao inicio() {
    inteiro idade
    real peso
    logico tatuagem, alcool

    escreva("Qual sua idade: ")
    leia(idade)

    se(idade < 19 ou idade > 69) {
      escreva("Infelizmente, você não pode ser doador.")
    } senao {
      escreva("Qual seu peso: ")
      leia(peso)
      se(peso < 50) {
        escreva("Infelizmente, você não pode ser doador.")
      } senao {
        escreva("Você fez alguma tatuagem no último ano? (verdadeiro ou falso): ")
        leia(tatuagem)
        se(tatuagem == verdadeiro) {
          escreva("Infelizmente, você não pode ser doador.")
        } senao {
          escreva("Você ingeriu álcool nas últimas 12 horas? (verdadeiro ou falso): ")
          leia(alcool)
          se(alcool == verdadeiro) {
            escreva("Infelizmente, você não pode ser doador.")
          } senao {
            escreva("Parabéns, você pode doar sangue.")
          }
        }
      }
    }
  }
}
